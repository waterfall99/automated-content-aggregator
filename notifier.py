import os
import requests
import database
from dotenv import load_dotenv
load_dotenv()

def send_notification(articles):
    WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
    if WEBHOOK is None:
        return False
    for article in articles:
        string_payload = f"**Source: \n{article[1]}\n{article[2]}\n{article[3]}**"
        try: 
            requests.post(WEBHOOK, json={"content":string_payload})
        except:
            return False  
    return True