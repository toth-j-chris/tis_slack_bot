blocks = """
{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This is a section block with a button."
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Click Me",
					"emoji": true
				},
				"value": "click_me_123",
				"action_id": "button-action"
			}
		}
	]
}
"""
# Client that reaches out to Virustotal to get context
# about ip addresses

import requests

class VirustotalClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_ip_context_list(self, ip_addresses):
        ip_context_list = []
        headers = { "x-apikey" : f"{self.api_key}"}
        session = requests.Session()
        session.headers.update(headers)
        for ip_address in ip_addresses:
            request_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
            response = session.get(request_url, headers=headers)
            if response.status_code == 200:
                ip_context_list.append(response.text)
            else:
                print(f"ERROR:: {response.status_code} :: {response.text}")

        return ip_context_list