# WordPress-6.9.1-Blind-SSRF
The exploit has no cve assigned.

Affected Versions
- 6.8 - 6.8.3
- 6.9 - 6.9.1

WordPress &lt;= 6.9.1 - Unauthenticated Blind SSRF via XML-RPC Pingback Discovery proof of concept (PoC)

# Usage
1. Install requests if not yet installed  `pip install requests`
2. Change config variables inside the code (e.g `WORDPRESS_URL`, `TARGET_POST` and `CALLBACK_URL`)
3. Execute script `python main.py`