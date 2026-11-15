import sqlite3

def init_db():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS articles 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        link TEXT UNIQUE NOT NULL,
        source TEXT,
        sent INTEGER DEFAULT 0)""")
    conn.commit()
    conn.close()
def save_articles(articles):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    for article in articles:
        cursor.execute("INSERT OR IGNORE INTO articles(title, link, source) VALUES (?, ?, ?)", (article["title"], article["link"], article["source"]))
    conn.commit()
    conn.close()
def get_unsent_articles():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, link, source FROM articles WHERE sent = 0")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows
def mark_as_sent(article_ids):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    for article_id in article_ids:
        cursor.execute("UPDATE articles SET sent = 1 WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    init_db()
    save_articles([{"title": "Test", "link": "https://example.com", "source": "Test"}, {"title": "Test", "link": "https://example.com", "source": "Test"}])
    print(get_unsent_articles())
    mark_as_sent([1])
    print(get_unsent_articles())