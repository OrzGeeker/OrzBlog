import json
import request
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    return json.loads('{"data":"translated text"}')

