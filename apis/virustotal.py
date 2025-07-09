import requests
from apis.utils import get_vt_key

def check_virustotal(sha256):
    headers = {"x-apikey": get_vt_key()}
    url = f"https://www.virustotal.com/api/v3/files/{sha256}"
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 404:
            return {"error": "File not found"}
        data = resp.json()["data"]["attributes"]["last_analysis_stats"]
        return data
    except Exception as e:
        return {"error": str(e)}