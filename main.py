import streamlit as st
from apis.utils import get_sha256
from apis import virustotal, koodous, urlscan, phishtank, threatfox, hybrid_analysis, google_safe_browsing

st.title("Threat Scanner: APKs & URLs")
tab1, tab2 = st.tabs(["APK Scanner", "URL Scanner"])

with tab1:
    uploaded_file = st.file_uploader("Upload an APK", type="apk")
    if uploaded_file:
        file_bytes = uploaded_file.read()
        sha256 = get_sha256(file_bytes)
        st.info(f"SHA-256: {sha256}")

        st.subheader("VirusTotal")
        st.json(virustotal.check_virustotal(sha256))

        st.subheader("Koodous")
        st.json(koodous.search_koodous(sha256))

        st.subheader("Hybrid Analysis")
        st.json(hybrid_analysis.scan_file_hybrid(file_bytes))
        
with tab2:
    url = st.text_input("Enter a URL or IP to scan")
    if url:
        st.subheader("VirusTotal")
        st.json(virustotal.check_virustotal(get_sha256(url.encode())))

        st.subheader("URLScan.io")
        st.json(urlscan.scan_url_urlscan(url))

        st.subheader("PhishTank")
        st.json(phishtank.check_phishtank(url))

        st.subheader("Google Safe Browsing")
        st.json(google_safe_browsing.check_safe_browsing(url))

        st.subheader("ThreatFox (IP Check)")
        st.json(threatfox.check_threatfox_ip(url))