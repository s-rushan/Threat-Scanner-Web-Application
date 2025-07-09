import requests
def check_phishtank(url):
    try:
        payload = {"url": url, "format": "json"}
        r = requests.post("http://checkurl.phishtank.com/checkurl/", data=payload)
        if "phish_detail_page" in r.text:
            return {"verdict": "phishing"}
        return {"verdict": "safe"}
    except Exception as e:
        return {"error": str(e)}