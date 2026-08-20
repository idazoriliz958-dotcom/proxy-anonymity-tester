# Proxy Anonymity & Header Leak Tester

A lightweight Python utility to test if your proxies are truly "Elite" (High Anonymity) or if they are secretly leaking your real IP to target servers.

## The Problem: Fake "Elite" Proxies
Many proxy providers advertise their IPs as "Elite". However, when you use them in your scraper, you still get blocked. Why? 

Because many poorly configured proxies inject specific HTTP headers into your requests before forwarding them to the target server. If the target server sees headers like `X-Forwarded-For` or `Via`, it instantly knows:
1. You are using a proxy.
2. What your real IP address is.

This repository provides a quick local script to parse the exact headers your proxy is sending to the destination.

## Quick Start (Local Header Test)

This script sends a request through your proxy to an echo server (`httpbin.org`) to reveal the exact HTTP headers the destination server receives.

**Installation:**
```bash
pip install requests
```
**Run the script:**
Create a tester.py file (see code below) and run:
```bash
python tester.py
```
## Advanced Leak Detection (Browser-Level)

While the Python script above is perfect for detecting basic HTTP header leaks (like X-Forwarded-For), it cannot detect browser-level leaks.
If you are using headless browsers (Playwright, Puppeteer, Selenium) or anti-detect browsers, your real IP can still leak through:

WebRTC Leaks (Bypasses HTTP proxies entirely)
DNS Leaks (Resolving hostnames via your local ISP instead of the proxy)
Timezone & Geolocation Mismatches

For full-stack browser anonymity testing, you need a visual diagnostic tool. I highly recommend running your proxy through the Rola IP Proxy Anonymity Checker. It provides a comprehensive breakdown of WebRTC vulnerabilities, real IP exposure, and exactly how target sites score your anonymity level.

## Local Script Code (tester.py)
See the included tester.py for the full HTTP header inspection logic. Feel free to add more leak-detection headers to the array if you know of any!
