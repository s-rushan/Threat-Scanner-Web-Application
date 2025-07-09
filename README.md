# Threat Scanner

A Streamlit web application for scanning APK files and URLs using multiple threat intelligence APIs. Instantly check files and links for malware, phishing, and other security threats.

## Features
- **APK Scanner:** Upload APK files and scan them with VirusTotal, Koodous, and Hybrid Analysis.
- **URL Scanner:** Enter a URL or IP address to check against VirusTotal, URLScan.io, PhishTank, Google Safe Browsing, and ThreatFox.
- **API Key Rotation:** Automatically rotates API keys to avoid rate limits.
- **Real-Time Results:** Displays scan results in a user-friendly JSON format.

## Setup
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd apk_scanner
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure API Keys:**
   - Edit `config.py` and add your API keys for each service.

## Running the App
```sh
streamlit run main.py
```
- The app will open in your browser.
- Use the APK Scanner tab to upload APKs.
- Use the URL Scanner tab to check URLs or IPs.

## Project Structure
```
├── main.py              # Streamlit app entry point
├── config.py            # API keys configuration
├── requirements.txt     # Python dependencies
└── apis/                # API integration modules
```

## Supported APIs
- VirusTotal
- Koodous
- Hybrid Analysis
- URLScan.io
- PhishTank
- Google Safe Browsing
- ThreatFox

## License
MIT License
