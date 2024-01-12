#!/usr/bin/env python3
"""basic flask app module"""


from flask import Flask
from flask import render_template

app = Flask(__name__)


@route('/', strict_slashes=False)
def index() -> str:
    """Render template that says hello world"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
