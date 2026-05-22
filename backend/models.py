from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
import datetime

## post table inside trends
class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True)
    subreddit = Column(String)
    title = Column(Text)
    body = Column(Text)
    author = Column(String)
    score = Column(Integer)
    num_comments = Column(Integer)
    created_utc = Column(DateTime)
    url = Column(Text)

    inserted_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )