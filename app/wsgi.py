from flask import Flask

from flask_smorest import Api

from app.resources.url import blp


def ping():
    return 'pong', 200, {
        'Content-Type': 'text/plain',
    }


def create_wsgi_app() -> Flask:
    app = Flask(__name__)
    app.config["API_TITLE"] = "My API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.secret_key = 'jose'
    app.route(ping)

    api = Api(app)

    # app.register_blueprint(blp)
    api.register_blueprint(blp)

    # CORS(app, origins=configuration.cross_origin)
    return app
