import requests

class VirustotalClient:
	"""Client that reaches out to Virustotal to get context about ip addresses"""

	def __init__(self, api_key, endpoint):
		"""Initialize with an api_key and the root endpoint of the api"""
		self.api_key = api_key
		self.endpoint = endpoint

	def get_ip_context_list(self, ip_addresses):
		"""Takes a list of ip addresses and gets context for each one from Virustotal"""

		ip_context_list = []
		headers = { "x-apikey" : f"{self.api_key}"}

		# Creating a session in case we're sending multiple requests 
		session = requests.Session()
		session.headers.update(headers)

		for ip_address in ip_addresses:
			request_url = f"{self.endpoint}/ip_addresses/{ip_address}"
			response = session.get(request_url, headers=headers)
			if response.status_code == 200:
				ip_context_list.append(response.text)
			else:
				print(f"ERROR:: {response.status_code} :: Error getting data for {ip_address}: {response.text}")

		return ip_context_list