import os
import time
import schedule
from slack_sdk import WebClient
from datetime import datetime

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID")

if not SLACK_BOT_TOKEN or not SLACK_CHANNEL_ID:
    raise ValueError("Slack token or channel ID not set")

client = WebClient(token=SLACK_BOT_TOKEN)

def send_reminder():
    print("Sending reminder at:", datetime.now())
    client.chat_postMessage(
        channel=SLACK_CHANNEL_ID,
        text="8 PM Reminder!\n1. GitHub ma `git pull` ra `git push` garna nabirsinu\n2. Output Emulator side by side rakhera garnus hai"
    )

# Nepal time is server time independent
schedule.every().day.at("20:00").do(send_reminder)

print("Slack bot started. Waiting for 8 PM...")

while True:
    schedule.run_pending()
    time.sleep(30)
