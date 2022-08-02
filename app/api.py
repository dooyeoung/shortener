from flask import Blueprint, jsonify, request, redirect
from werkzeug.exceptions import BadRequest

from app.context import url_service


api = Blueprint('api', __name__,)


@api.route('/ping')
def ping():
    return 'pong', 200, {
        'Content-Type': 'text/plain',
    }

@api.route('/<string:short_id>')
def redirect_to_long_url(short_id):
    source_url = url_service.get_source_url(short_id)
    return redirect(source_url)


@api.route('/api/shorten', methods=["POST"])
def shorten():
    req = request.json
    url = req.get("url", None)
    if not url:
        raise BadRequest

    short_url = url_service.shorten(url)
    return jsonify({"short_url": short_url})
