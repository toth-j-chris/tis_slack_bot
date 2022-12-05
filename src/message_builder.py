import json

def build_reply_message(ip_context_list):
    num_ip_addresses = len(ip_context_list)
    exclude_attributes = {
        "last_analysis_results",
        "last_https_certificate",
        "whois"
        }
    reply_text = f"""
Found {num_ip_addresses} IP address{'es' if num_ip_addresses > 1 else ''} in your message!
Here is some additional context about these IPs, provided by Virustotal:
    """
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