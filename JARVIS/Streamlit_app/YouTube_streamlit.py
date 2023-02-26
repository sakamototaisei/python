from apiclient.discovery import build
import json
import streamlit as st

import YouTube_data_function

# jsonファイルからAPIKEYの取得
with open('JARVIS/Streamlit_app/jarvis-youtube.json') as f:
    secret = json.load(f)

DEVELOPER_KEY = secret['KEY']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
# 認証を行っている
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

st.title('YouTube分析アプリ')

st.sidebar.write('## クエリと閾値の設定')
st.sidebar.write('## クエリの入力')
query = st.sidebar.text_input('検索クエリを入力してください', 'コレコレ')

st.sidebar.write('### 閾値の設定')
threshold = st.sidebar.slider('登録者の閾値', 1000, 1000000, 100000)

st.write('### 選択中のパラメータ')
st.markdown(f"""
- 検索クエリ： {query}
- 登録者数の閾値： {threshold}
""")

df_video = YouTube_data_function.video_search(youtube, q=query, max_results=50)
results = YouTube_data_function.get_results(
    youtube, df_video, threshold=threshold)

st.write('### 分析結果', results)
