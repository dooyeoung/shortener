import typing
from sqlalchemy.engine import Connection, Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DATABASE = dict(
        url = "postgresql://localhost/shortener_study"
    )
    BASE_URL = "http://127.0.0.1:9999/"


def create_database_engine_with_config(database_config: dict) -> Engine:
    db_options = database_config.copy()
    url = db_options.pop("url")
    return create_engine(url, **db_options)

def create_database_session(
    database_config,
):
    bind = create_database_engine_with_config(database_config)
    return sessionmaker()(bind=bind)
