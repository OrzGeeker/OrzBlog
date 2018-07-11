#!/usr/bin/env bash

git clean -dfx
virtualenv venv
. venv/bin/activate
pip install -r requirement.txt
flask db upgrade
flask run --host=0.0.0.0
