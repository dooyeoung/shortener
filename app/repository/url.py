import abc
from typing import Optional

from sqlalchemy.orm.session import Session

from app.models.url import Url

class UrlRepository(abc.ABC):
    @abc.abstractmethod
    def get_url_by_source_url(
        self, session: Session, **path_parameters
    ) -> Optional[Url]:
        pass

    
    def get_url_by_short_id(
        self, session: Session, **path_parameters
    ) -> Optional[Url]:
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
        ).one_or_none()


    def get_url_by_short_id(
        self,
        session: Session,
        short_id: str,
    ) -> Optional[Url]:
        return session.query(
            Url
        ).filter(
            Url.short_id == short_id
        ).one_or_none()