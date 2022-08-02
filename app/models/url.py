from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import String
from sqlalchemy.types import Boolean, DateTime, Integer, Unicode

Base = declarative_base()

class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    short_id = Column(String(7), unique=True)
    source_url = Column(String(255), nullable=False)
