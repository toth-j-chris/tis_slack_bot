import json

from ip_parser import parse_ips
from message_builder import build_reply_message

class EventHandler:
    """Handles events that are generated from the slack bolt app"""

    def __init__(self, virustotal_client):
        """Constructor that takes an instance of a VirustotalClient"""

        self.virustotal_client = virustotal_client

    def handle_message(self, event, say):
        """Handles a message event 
        """
        message_text = event["text"]
        ip_addresses = parse_ips(message_text)
        if ip_addresses:
            ip_context_list = self.virustotal_client \
                .get_ip_context_list(ip_addresses)
            if len(ip_context_list) > 0:
                reply_text = self.__build_reply_text(ip_context_list)
                thread_ts = event["ts"]
                say(
                    text=reply_text,
                    thread_ts=thread_ts, 
                )