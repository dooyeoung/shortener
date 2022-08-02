from urllib.parse import urljoin

from app.repository.url import UrlRepository
from app.models.url import Url

# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 으로 구성
BASE62 = "dCsuHTIWEcOPLhrgwBpRx4flv8JMKGDVmQ01qtejY9iNFzn5okX63aZAbySU27"
SHORTENER_ID_LENGTH = 7

class UrlService():
    def __init__(
        self,
        url_repository: UrlRepository,
        session,
        base_url
    ):
        self.url_repository = url_repository
        self.session = session
        self.base_url = base_url


    def encode(self, num, alphabet=BASE62):
        """Encode a positive number into Base X and return the string.

        Arguments:
        - `num`: The number to encode
        - `alphabet`: The alphabet to use for encoding
        """
        if num == 0:
            return alphabet[0]
        arr = []
        arr_append = arr.append  # Extract bound-method for faster access.
        _divmod = divmod  # Access to locals is faster.
        base = len(alphabet)
        while num:
            num, rem = _divmod(num, base)
            arr_append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    def decode(self, string, alphabet=BASE62):
        """Decode a Base X encoded string into the number

        Arguments:
        - `string`: The encoded string
        - `alphabet`: The alphabet to use for decoding
        """
        base = len(alphabet)
        strlen = len(string)
        num = 0

        idx = 0
        for char in string:
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1

        return num

    def shorten(self, source_url):
        result = self.url_repository.get_url_by_source_url(
            source_url=source_url,
            session=self.session
        )

        # 기존에 있는 url이라면 그대로 반환
        if result:
            short_id = result.short_id
        else:
            url = Url(source_url=source_url)
            self.session.add(url)
            self.session.flush()

            encoded = self.encode(url.id)
            short_id = BASE62[0] * (SHORTENER_ID_LENGTH - len(encoded)) + encoded

            url.short_id = short_id
            self.session.commit()

        return urljoin(self.base_url, short_id)

    
    def get_source_url(self, short_id):
        return self.url_repository.get_url_by_short_id(
            session=self.session,
            short_id=short_id,
        ).source_url