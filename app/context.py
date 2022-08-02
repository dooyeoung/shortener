import typing

from flask import current_app, has_request_context, request
from sqlalchemy.orm.session import Session
from werkzeug.local import LocalProxy
from werkzeug.wrappers import Request

from app.orm import database_sessionmaker
from app.repository.url import SQLAlchemyUrlRepository
from app.service.url import UrlService


def get_app_context() -> typing.Tuple[
    typing.Union[Request, None],
]:
    if has_request_context():
        ctx = request._get_current_object()
        app_config = current_app.config

    return app_config, ctx


def get_config():
    return get_app_context()[0]


@LocalProxy
def url_repository():
    app_config, ctx = get_app_context()
    url_repository = getattr(ctx, "_url_repository", None)
    if url_repository is None:
        url_repository = SQLAlchemyUrlRepository()
        setattr(ctx, "_url_repository", url_repository)
    return url_repository


@LocalProxy
def url_service():
    app_config, ctx = get_app_context()
    url_service = getattr(ctx, "_url_service", None)
    if url_service is None:
        url_service = UrlService(
            url_repository=url_repository,
            sessionmaker=database_sessionmaker(
                app_config["DATABASE"]
            ),
            base_url=app_config["BASE_URL"],
        )
        setattr(ctx, "_url_service", url_service)
    return url_service
