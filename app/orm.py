import contextlib

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker


@contextlib.contextmanager
def session_scope(sesionmaker: sessionmaker):
    """Provide a transactional scope around a series of operations."""
    session = sesionmaker()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def database_engine(database_config: dict) -> Engine:
    db_options = database_config.copy()
    url = db_options.pop("url")
    return create_engine(url, **db_options)

def database_sessionmaker(
    database_config,
):
    bind = database_engine(database_config)
    return sessionmaker(
        bind=bind,
        expire_on_commit=False,
    )
