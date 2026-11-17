from fetcher import fetch_articles
from database import init_db, save_articles, get_unsent_articles, mark_as_sent
from notifier import send_notification
import os

def main():
    new_articles_to_send = []
    fetched_articles = fetch_articles()
    save_articles(fetched_articles)
    new_rows = get_unsent_articles()
    if send_notification(new_rows):
        all_rows = []
        for row in new_rows:
            all_rows.append(row[0])
        mark_as_sent(all_rows)

if __name__ == "__main__":
    main()
        


