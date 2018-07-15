#!/usr/bin/env bash

killall redis-server
git clean -dfx
virtualenv venv
. venv/bin/activate
pip install -r requirement.txt
flask db upgrade
redis-server &
rq worker microblog-tasks &
flask run --host=0.0.0.0
