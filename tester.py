```python
import requests
import json

def test_proxy_anonymity(proxy_url):
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    
    # Headers that typically reveal client IP or proxy usage
    leak_headers_to_check = [
        'X-Forwarded-For', 
        'X-Real-Ip', 
        'Via', 
        'Forwarded',
        'X-ProxyUser-Ip'
    ]

    print(f"Testing Proxy: {proxy_url} ...\n")

    try:
        # httpbin.org/headers returns the exact headers it received from the client/proxy
        response = requests.get("https://httpbin.org/headers", proxies=proxies, timeout=10)
        
        if response.status_code == 200:
            received_headers = response.json().get("headers", {})
            leaks_found = {}

            # Check if any leak headers exist in the payload
            for header, value in received_headers.items():
                if header in leak_headers_to_check:
                    leaks_found[header] = value

            if leaks_found:
                print("🚨 [WARNING] - TRANSPARENT / ANONYMOUS PROXY DETECTED!")
                print("The target server can see the following injected headers:")
                print(json.dumps(leaks_found, indent=4))
                print("Your real IP might be exposed.\n")
            else:
                print("✅ [SUCCESS] - ELITE PROXY DETECTED!")
                print("No standard IP-leaking headers were found in the request.\n")
        else:
            print(f"Failed to connect. Status code: {response.status_code}")

    except Exception as e:
        print(f"❌ [ERROR] Proxy failed to connect or timed out. Details: {e}")

if __name__ == "__main__":
    # Replace with your proxy
    TEST_PROXY = "http://username:password@ip:port" 
    test_proxy_anonymity(TEST_PROXY)
