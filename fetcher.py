from config import FEED_URLS, KEYWORDS
import feedparser
def fetch_articles():
    matched_articles = []
    for url in FEED_URLS:
        print(f"Fetching {url}...")
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.get("title", "")
            for keyword in KEYWORDS:
                if keyword.lower() in title.lower():
                    matched_articles.append({"title": title, "link": entry.get("link", ""), "source": feed.feed.get("title", url)})
                    break
    return matched_articles
if __name__ == "__main__":
    print(fetch_articles())

