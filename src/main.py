import os

from event_handler import EventHandler 
from virustotal_client import VirustotalClient

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

def main():
    # Load environment variables from .env
    load_dotenv()

    try:
        SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
        SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
        VIRUSTOTAL_API_KEY = os.environ['VIRUSTOTAL_API_KEY']

        virustotal_client = VirustotalClient(VIRUSTOTAL_API_KEY)
        event_handler = EventHandler(virustotal_client)

        # Initialize slack bolt app with the bot token
        app = App(token=SLACK_BOT_TOKEN)

        # Event that triggers when a message is sent 
        @app.event("message")
        def handle_message_event(event, say):
            event_handler.handle_message(event, say)

        # Start the app in Socket Mode
        SocketModeHandler(app, SLACK_APP_TOKEN).start()

    except KeyError as key_error:
        print(f"Missing environment variable. Please add a {key_error} to your .env file.")

if __name__ == "__main__":
    main()