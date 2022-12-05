import re

ipv4_regex_string = """
((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))
"""

# Compile the regex pattern when the file is imported, rather than every time parse_ips is called
ipv4_regex_pattern = re.compile(ipv4_regex_string, re.VERBOSE)

def parse_ips(message_string):
    """Handles parsing ip addresses out of message strings"""

    ip_addresses = ipv4_regex_pattern.findall(message_string)

    return ip_addresses