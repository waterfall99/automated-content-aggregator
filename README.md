# Automated Content Aggregator

An automated Python tool that collects articles from multiple websites, filters them based on specific keywords, and delivers a curated digest straight to your email inbox every morning.

## Features
* **Multi-Source Fetching:** Automatically pulls new articles from a customizable list of RSS feeds and websites.
* **Keyword Filtering:** Scans article titles and summaries to match your specific topics of interest.
* **Duplicate Prevention:** Tracks previously sent articles in a local database so you never receive the same story twice.
* **Daily Morning Digest:** Formats matching articles into a clean summary and emails them to your inbox on a daily schedule.

## Project Structure
* **`config.py`:** Stores target feed URLs, keyword lists, and general settings.
* **`fetcher.py`:** Connects to websites and RSS feeds to retrieve the latest articles.
* **`database.py`:** Manages the local SQLite database to log seen articles and prevent duplicates.
* **`notifier.py`:** Formats the filtered articles and handles sending the daily email digest.
* **`main.py`:** Coordinates the entire pipeline from fetching to emailing.
* **`.env`:** Stores sensitive credentials (not tracked in version control).

## Setup & Installation

1. **Clone the repository**
   Download the project files to your local machine and navigate into the project folder.

2. **Install dependencies**
   Install the required Python packages listed in your `requirements.txt` file (such as `feedparser`, `python-dotenv`, and `requests`).

3. **Configure environment variables**
   Create a `.env` file in the root directory and add your email credentials:
   * `EMAIL_ADDRESS` — The email address sending/receiving the digest
   * `EMAIL_PASSWORD` — Your app password or SMTP credential
   * `SMTP_SERVER` — Your email provider's SMTP server address
   * `SMTP_PORT` — Your email provider's SMTP port

4. **Customize your feeds and keywords**
   Open `config.py` to add your preferred website feed URLs and target keywords.

## Usage
* **Manual Run:** Execute `main.py` from your terminal to run the aggregator immediately and send out any new matching articles.
* **Automated Schedule:** Set up a daily scheduled task (using Windows Task Scheduler, cron, or GitHub Actions) to trigger `main.py` automatically every morning.
