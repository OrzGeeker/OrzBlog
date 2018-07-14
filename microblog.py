from app.models import User, Post
from app import cli, create_app,db
from app.models import Notification, Message

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db':db,
            'User':User,
            'Post':Post,
            'Message':Message,
            'Notification':Notification}


