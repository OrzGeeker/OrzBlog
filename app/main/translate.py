import json
import request
from flask_babel import _

def translate(text, source_language, dest_language):
    return json.loads('{"data":"translated text"}')

