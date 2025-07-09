import requests
from config import HYBRID_ANALYSIS_KEY

def scan_file_hybrid(file_bytes):
    headers = {
        "api-key": HYBRID_ANALYSIS_KEY,
        "Content-Type": "application/octet-stream"
    }
    try:
        resp = requests.post("https://www.hybrid-analysis.com/api/v2/submit/file", headers=headers, data=file_bytes)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}