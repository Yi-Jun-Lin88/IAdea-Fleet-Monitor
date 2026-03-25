import streamlit as st
import pandas as pd
import requests
import io
import urllib3

# 關閉不安全請求的警告訊息（因為要跳過 SSL 驗證）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 頁面設定
st.set_page_config(page_title="Taipei Cardless Parking Monitor", layout="wide")

st.title("🅿️ 台北市 Pay.taipei 無卡進出停車場監控")
st.caption("Data Source：台北市資料大平台 (Real-time Open Data)")

# 設定資料來源 URL
CSV_URL = "https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=c0408caa-b6ae-47e7-b4e9-1d806afd69c2"


@st.cache_data(ttl=600)  # 快取資料 10 分鐘，避免頻繁請求 API
def load_taipei_data():
    try:
        # 加入 verify=False 跳過憑證檢查
        response = requests.get(CSV_URL, verify=False)
        response.encoding = response.apparent_encoding

        df = pd.read_csv(io.StringIO(response.text))
        return df
    except Exception as e:
        st.error(f"資料抓取失敗: {e}")
        return None


# 執行資料載入
df = load_taipei_data()

if df is not None:
    # 儀表板摘要
    # 假設「狀態」欄位中，'1' 或 '開啟' 代表服務正常
    total_sites = len(df)
    active_sites = len(df[df['狀態'].astype(str).str.contains('1|開啟|有效|正常', na=False)])

    col1, col2, col3 = st.columns(3)
    col1.metric("總計停車場數", total_sites)
    col2.metric("無卡進出服務中", active_sites)
    col3.metric("服務異常/維護中", total_sites - active_sites)

    st.divider()

    # 搜尋與篩選功能
    search_query = st.text_input("🔍 搜尋停車場名稱或地址", "")

    # 資料處理與顯示
    # 篩選後的數據
    if search_query:
        df = df[df['對應停車場'].str.contains(search_query, na=False) |
                df['地址'].str.contains(search_query, na=False)]


    # 定義狀態上色邏輯
    def style_status(val):
        # 如果狀態包含 '1' 或 '開啟'，顯示綠色，否則紅色
        is_active = str(val) in ['1', '開啟', '有效', '正常']
        color = '#2ecc71' if is_active else '#e74c3c'
        return f'color: {color}; font-weight: bold'


    # 重新排列欄位，方便閱讀重點
    display_cols = ['對應停車場', '狀態', '地址', '電話', '營運單位']
    available_cols = [c for c in display_cols if c in df.columns]

    st.dataframe(
        df[available_cols].style.map(style_status, subset=['狀態'] if '狀態' in df.columns else []),
        width="stretch",
        height=600
    )

    st.info("💡 提示：狀態顯示為綠色代表該場站目前支援 Pay.taipei 無卡進出服務。")
else:
    st.warning("暫時無法取得台北市政府開放資料，請稍後再試。")