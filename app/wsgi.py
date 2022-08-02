from flask import Flask
from app.api import api


def create_wsgi_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api)
    # CORS(app, origins=configuration.cross_origin)
    return app
