import requests
from apis.utils import get_koodous_key

def search_koodous(sha256):
    headers = {"Authorization": f"Token {get_koodous_key()}"}
    url = f"https://api.koodous.com/apks/{sha256}"
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 404:
            return {"error": "APK not found in Koodous"}
        data = resp.json()
        return {"verdict": data.get("verdict"), "score": data.get("score")}
    except Exception as e:
        return {"error": str(e)}