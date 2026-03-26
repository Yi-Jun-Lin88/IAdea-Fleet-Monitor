# 🅿️ Taipei Parking Fleet Monitor (Streamlit Version)

This project is a real-time data dashboard built for the **IAdea AI-Assisted Software Builder Challenge**. It monitors the "Pay.taipei Cardless Parking" status using Taipei City Open Data.

## 🌟 Key Features
- **Live Data Ingestion:** Fetches real-time CSV data from Taipei City Data Platform.
- **Robust Data Handling:** Implemented automatic encoding detection (Big5/UTF-8) and SSL verification bypass for government server compatibility.
- **Performance Optimization:** Utilizes Streamlit's `@st.cache_data` to reduce API overhead and improve loading speed.
- **Interactive UI:** Includes real-time search filtering and status-based conditional formatting.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Framework:** Streamlit
- **Libraries:** Pandas, Requests, Urllib3 (for SSL handling)

## 🚀 How to Run Locally
1. Clone the repo: `git clone https://github.com/你的帳號/IAdea-Fleet-Monitor.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

This project is hosted on **Streamlit**. 
Live Demo: [[My Streamlit URL]](https://iadea-fleet-monitor-5ztlqfzqmruymgczycfsvu.streamlit.app/)

<p align="center">
<img width="700" alt="截圖 2026-03-26 下午4 11 46" src="https://github.com/user-attachments/assets/a5b56b16-2032-48e7-8607-82a83e6c7c43" />
</p>

## 🤖 AI-Assisted Troubleshooting
- Successfully resolved `SSLCertVerificationError` by implementing a custom request handler with `verify=False` and warning suppression.
- Refactored deprecated Pandas syntax from `applymap` to `map` for future-proof compatibility.
