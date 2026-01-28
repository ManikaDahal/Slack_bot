import os
from slack_sdk import WebClient

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID")

if not SLACK_BOT_TOKEN or not SLACK_CHANNEL_ID:
    raise ValueError("Slack token or channel ID not set!")

client = WebClient(token=SLACK_BOT_TOKEN)

def send_reminder():
    try:
        client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text="8 PM Reminder!\n1. GitHub ma `git pull` ra `git push` garna nabirsinu \n2. Output Emulator side by side rakhera garnus hai"
        )
        print("Reminder sent!")
    except Exception as e:
        print("Failed to send reminder:", e)

if __name__ == "__main__":
    send_reminder()
