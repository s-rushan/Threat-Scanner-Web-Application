import requests
from config import ABUSEIPDB_KEY

def check_abuseip(ip):
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
    headers = {"Key": ABUSEIPDB_KEY, "Accept": "application/json"}
    try:
        r = requests.get(url, headers=headers)
        data = r.json()["data"]
        return {"abuseConfidenceScore": data["abuseConfidenceScore"]}
    except Exception as e:
        return {"error": str(e)}
