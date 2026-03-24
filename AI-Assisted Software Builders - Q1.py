import streamlit as st
import pandas as pd

# 設定頁面資訊
st.set_page_config(page_title="IAdea Fleet Monitor", layout="wide")

st.title("📊 IAdea Device Fleet Dashboard")
st.write("即時監控全方位設備狀態")

# CSV 網址
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRCoE7I08iRza6QrUuyDNqA6FFnCuuANjsBf6hogreujMgtZtPld4kichpuA-S592Gw2erVx5xLRCuR/pub?output=csv"

def load_data():
    df = pd.read_csv(CSV_URL)
    return df

try:
    data = load_data()

    # 建立上方摘要指標
    col1, col2, col3 = st.columns(3)
    col1.metric("總設備數", len(data))
    col2.metric("在線數", len(data[data['Status'] == 'Online']))
    col3.metric("離線數", len(data[data['Status'] == 'Offline']))

    # 數據過濾器
    status_filter = st.multiselect("過濾狀態", options=data["Status"].unique(), default=data["Status"].unique())
    filtered_data = data[data["Status"].isin(status_filter)]

    # 顯示表格並根據狀態上色（Streamlit 內建風格）
    def color_status(val):
        color = 'green' if val == 'Online' else 'red'
        return f'color: {color}; font-weight: bold'

    st.dataframe(filtered_data.style.map(color_status, subset=['Status']), width="stretch")

    if st.button('手動重新整理'):
        st.rerun()

except Exception as e:
    st.error(f"無法讀取數據，請檢查 CSV 網址是否正確。錯誤原因: {e}")
