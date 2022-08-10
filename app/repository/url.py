import abc
from re import T
from typing import Optional, Sequence

from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound

from app.models.url import Url
from app.exc import NotFoundUrl

class UrlRepository(abc.ABC):
    @abc.abstractmethod
    def get_url_by_source_url(
        self, session: Session, **parameters
    ) -> Optional[Url]:
        pass


    def get_url_by_short_id(
        self, session: Session, **parameters
    ) -> Url:
        pass


    def get_all(
        self, session: Session, **parameters
    ) -> Sequence[Url]:
        pass


class SQLAlchemyUrlRepository(UrlRepository):
    def get_url_by_source_url(
        self,
        session: Session, 
        source_url: str,
    ) -> Optional[Url]:
        return session.query(
            Url
        ).filter(
            Url.source_url == source_url
        ).first()


    def get_url_by_short_id(
        self,
        session: Session,
        short_id: str,
    ) -> Optional[Url]:
        datas = None
        try:
            datas = session.query(
                Url
            ).filter(
                Url.short_id == short_id
            ).one()
        except NoResultFound:
            raise NotFoundUrl
        return datas


    def get_all(
        self,
        session: Session,
    ) -> Sequence[Url]:
        return session.query(
            Url
        ).all()
