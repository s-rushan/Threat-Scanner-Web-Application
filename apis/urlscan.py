import requests
from apis.utils import get_urlscan_key

def scan_url_urlscan(url):
    headers = {
        "API-Key": get_urlscan_key(),
        "Content-Type": "application/json"
    }
    data = {"url": url, "visibility": "public"}
    try:
        r = requests.post("https://urlscan.io/api/v1/scan/", json=data, headers=headers)
        return r.json()
    except Exception as e:
        return {"error": str(e)}
