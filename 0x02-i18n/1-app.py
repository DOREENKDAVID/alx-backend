#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """Configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    # instanciate the app object
    app = Flask(__name__)
    app.config.from_object(Config)

    # wrap app with babel
    babel = Babel(app)

    @app.route('/', strict_slashes=False)
    def index() -> str:
        """
        Renders 1-index. html template
        """
        return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
