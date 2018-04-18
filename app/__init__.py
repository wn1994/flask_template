from flask import Flask
from werkzeug.utils import import_string
import default_config

# from .modules.main import main

blueprints = [
    'app.modules.main:main',
]


def create_app(config=None):
    app = Flask(__name__)
    configure_app(app, config)

    # load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app


def configure_app(app, config):
    app.config.from_object(default_config.BaseConfig)

    if not config:
        config = default_config.config_map['dev']

    app.config.update(config)
