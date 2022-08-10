from urllib.parse import urljoin

from app.base62 import BASE62, encode
from app.models.url import Url
from app.orm import session_scope
from app.repository.url import UrlRepository

SHORTENER_ID_LENGTH = 7

class UrlService():
    def __init__(
        self,
        url_repository: UrlRepository,
        sessionmaker,
        base_url
    ):
        self.url_repository = url_repository
        self.sessionmaker = sessionmaker
        self.base_url = base_url


    def get_all(self):
        with session_scope(self.sessionmaker) as session:
            return self.url_repository.get_all(
                session=session
            )


    def shorten(self, source_url):
        with session_scope(self.sessionmaker) as session:
            result = self.url_repository.get_url_by_source_url(
                source_url=source_url,
                session=session
            )
            # 기존에 있는 url이라면 그대로 반환
            if result:
                short_id = result.short_id
            else:
                url = Url(source_url=source_url)
                session.add(url)
                session.flush()
                encoded = encode(url.id)
                short_id = BASE62[0] * (SHORTENER_ID_LENGTH - len(encoded)) + encoded
                url.short_id = short_id

        return urljoin(self.base_url, short_id)


    def get_source_url(self, short_id):
        with session_scope(self.sessionmaker) as session:
            return self.url_repository.get_url_by_short_id(
                session=session,
                short_id=short_id,
            ).source_url
