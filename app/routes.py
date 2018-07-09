from flask import render_template
from flask import request, g, jsonify
from flask import flash, redirect, url_for

from flask_login import current_user
from flask_login import login_required

from flask_babel import _
from flask_babel import get_locale

from datetime import datetime

from app import app
from app import db
from app.forms import PostForm
from app.forms import EditProfileForm
from app.models import User
from app.models import Post
from app.translate import translate
from guess_language import guess_language

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale=str(get_locale())

@app.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        language=guess_language(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language=''
        post = Post(body=form.post.data,
                    author=current_user,
                    language=language)
        db.session.commit()
        flash(_('Your post is now live'))
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
    page,app.config['POSTS_PER_PAGE'], False)
    next_url=url_for('index', page = posts.next_num) if posts.has_next else None
    prev_url=url_for('index', page = posts.prev_num) if posts.has_prev else None

    return render_template('index.html',
                           title='Home Page',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    page,app.config['POSTS_PER_PAGE'], False)
    next_url=url_for('user', username=username, page = posts.next_num) if posts.has_next else None
    prev_url=url_for('user', username=username, page = posts.prev_num) if posts.has_prev else None
    return render_template('user.html',
                           user=user,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)


@app.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('user',username=current_user.username))
    elif request.method=='GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title = 'Edit Profile',form=form)

@app.route('/follow/<username>')
@login_required
def follow(username):
    user =  User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.',username=username))
        return redirect(url_for('index'))
    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('user',username=username))
    current_uesr.follow(username)
    db.session.commit()
    flash(_('You are following %(username)s',username=username))
    return redirect(url_for('user',username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.',username=username))
        return redirect(url_for('index'))
    if user == current_user:
        flash(_('You cannot unfollow %(username)s',username=username))
        return redirect(url_for('user',username=username))
    current_user.unfollow(user)
    flash(_('You are not following %(username)s',username=username))
    return redirect(url_for('user',username=username))

@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    page,app.config['POSTS_PER_PAGE'], False)
    next_url=url_for('index', page = posts.next_num) if posts.has_next else None
    prev_url=url_for('index', page = posts.prev_num) if posts.has_prev else None
    return render_template('index.html',
                           title = 'Explore',
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)

