## utilizing VADER for sentiment analysis 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from database import SessionLocal
from models import Post

sid_obj = SentimentIntensityAnalyzer()

db = SessionLocal()
posts = db.query(Post).all()

for post in posts:
    sentiment = sid_obj.polarity_scores(post.title)
    compound = sentiment["compound"]

    if compound >= .05:
        label = "positive"
    elif compound <= -.05:
        label = "negative"
    else:
        label = "neutral"

    print(f"{label.upper()} | {compound} | {post.title}")

db.close()