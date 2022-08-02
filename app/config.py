class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DATABASE = dict(
        url = "postgresql://localhost/shortener_study"
    )
    BASE_URL = "http://127.0.0.1:9999/"
