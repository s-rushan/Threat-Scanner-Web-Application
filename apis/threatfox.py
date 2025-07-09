import requests

def check_threatfox_ip(ip):
    url = "https://threatfox.abuse.ch/api/v1/"
    payload = {"query": "search_ioc", "search_term": ip}
    try:
        response = requests.post(url, data=payload)
        data = response.json()
        if data["query_status"] == "no_results":
            return {"verdict": "clean"}
        else:
            return {
                "verdict": "malicious",
                "ioc_count": len(data["data"]),
                "threat_types": list(set([entry["threat_type"] for entry in data["data"]]))
            }
    except Exception as e:
        return {"error": str(e)}