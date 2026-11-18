import logging
import os

log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aggregator.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
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
    logging.info("--- Aggregator script started ---")
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
    except Exception as e:
        logging.error(f"Application crashed: {e}")
    logging.info("Aggregator run completed successfully.")
if __name__ == "__main__":
    main()
        


