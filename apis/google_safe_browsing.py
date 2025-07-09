import requests
from config import GOOGLE_SAFE_BROWSING_KEY

def check_safe_browsing(url):
    body = {
        "client": {"clientId": "myapp", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    try:
        resp = requests.post(
            f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_SAFE_BROWSING_KEY}",
            json=body
        )
        matches = resp.json().get("matches")
        return {"verdict": "unsafe" if matches else "safe"}
    except Exception as e:
        return {"error": str(e)}
