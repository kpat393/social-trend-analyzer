import requests
from datetime import datetime

from database import SessionLocal, Base, engine
from models import Post

Base.metadata.create_all(bind=engine)

SUBREDDITS = ["ChatGPT", "singularity", "artificial", "Futurology"]

headers = {
    "User-Agent": "social-trend-analyzer/0.1"
}

db = SessionLocal()

for subreddit_name in SUBREDDITS:
    url = f"https://www.reddit.com/r/{subreddit_name}/hot.json?limit=10"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch r/{subreddit_name}: {response.status_code}")
        continue

    posts = response.json()["data"]["children"]

    for item in posts:
        data = item["data"]

        post = Post(
            id=data["id"],
            subreddit=data["subreddit"],
            title=data["title"],
            body=data.get("selftext", ""),
            author=str(data.get("author", "")),
            score=data["score"],
            num_comments=data["num_comments"],
            created_utc=datetime.utcfromtimestamp(data["created_utc"]),
            url=data["url"],
        )

        db.merge(post)

db.commit()
db.close()

print("Inserted public Reddit posts successfully.")