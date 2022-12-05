import json

from ip_parser import parse_ips

class EventHandler:
    """Handles events that are generated from the slack bolt app"""

    def __init__(self, virustotal_client):
        """Constructor that takes an instance of a VirustotalClient"""

        self.virustotal_client = virustotal_client

    def handle_message(self, event, say):
        """If one or more IP addresses are found in the message, replies with context about them""" 

        message_text = event["text"]
        ip_addresses = parse_ips(message_text)

        if len(ip_addresses) == 0:
            return

        ip_context_list = self.virustotal_client.get_ip_context_list(ip_addresses)

        if len(ip_context_list) > 0:
            reply_text = self.__build_reply_message(ip_context_list)
            thread_ts = event["ts"]
            say(
                text=reply_text,
                thread_ts=thread_ts, 
            )
    
    def __build_reply_message(self, ip_context_list):
        """Creates a reply message out of the IP context"""

        num_ip_addresses = len(ip_context_list)

        # These attributes are very long, so they are excluded from the reply for readability
        exclude_attributes = {
            "last_analysis_results",
            "last_https_certificate",
            "whois"
            }

        reply_text = f"Found {num_ip_addresses} IP address{'es' if num_ip_addresses > 1 else ''} in your message!" + \
        "Here is some additional context about these IPs, provided by Virustotal:"

        # For every ip address, print it's value then add each attribute from Virustotal
        # if the attribute is not in the exclude_attributes set
        for ip_context in ip_context_list:
            ip_context_data = json.loads(ip_context)["data"]
            ip_context_attributes = ip_context_data["attributes"]
            reply_text += f"\n`{ip_context_data['id']}`\n```"
            for attribute in ip_context_attributes:
                if attribute not in exclude_attributes:
                    attribute_value = json.dumps(
                        ip_context_attributes[attribute],
                        sort_keys=True, 
                        indent=4
                        )
                    reply_text += f"{attribute} : {attribute_value}\n"
            reply_text += "```"
        reply_text += "\n\nSome data excluded for readability :smile:"

        return reply_text