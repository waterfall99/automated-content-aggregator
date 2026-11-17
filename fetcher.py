import logging
from config import FEED_URLS, KEYWORDS
import feedparser
def fetch_articles():
    matched_articles = []
    for url in FEED_URLS:
        logging.info(f"Fetching {url}...")
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                title = entry.get("title", "")
                for keyword in KEYWORDS:
                    if keyword.lower() in title.lower():
                        matched_articles.append({"title": title, "link": entry.get("link", ""), "source": feed.feed.get("title", url)})
                        break
        except Exception as e:
            logging.error(f"Failed to fetch feed {url}: {e}")
    return matched_articles
if __name__ == "__main__":
    logging.info(fetch_articles())

