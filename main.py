import os
import logging
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'aggregator.log')
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
from fetcher import fetch_articles
from database import init_db, save_articles, get_unsent_articles, mark_as_sent
from notifier import send_notification

logging.basicConfig(
    filename="aggregator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)% - %(message)%"
)

def main():
    try:
        init_db()
        fetched_articles = fetch_articles()
        save_articles(fetched_articles)
        new_rows = get_unsent_articles()
        if new_rows:
            if send_notification(new_rows):
                all_rows = []
                for row in new_rows:
                    all_rows.append(row[0])
                mark_as_sent(all_rows)
            logging.info("Aggregator run completed successfully.")
    except Exception as e:
        logging.error(f"Application crashed: {e}")
if __name__ == "__main__":
    main()
        


