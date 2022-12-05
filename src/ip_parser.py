import re

def parse_ips(message_string):
    """Handles parsing ip addresses out of message strings"""

    ipv4_regex_string = """
    ((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))
    """

    ipv4_regex_pattern = re.compile(ipv4_regex_string, re.VERBOSE)

    ip_addresses = ipv4_regex_pattern.findall(message_string)
    test(ip_addresses, message_string)

    if len(ip_addresses) > 0:
        return ip_addresses

    return None