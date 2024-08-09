import streamlit as st
import time

st.title("翻訳アプリ")
source_languages = ["英語", "日本語"]

row1_left, row1_center, row1_right = st.columns((4, 0.5, 4))
row2_left, row2_right = st.columns(2)

with row1_left:
    source = st.selectbox(
        'ソース言語',
        source_languages,
        label_visibility="collapsed"
    )

with row1_center:
    if st.button("↔️", type="secondary", use_container_width=True):
        pass

with row1_right:
    target_languages = [l for l in source_languages if l != source]
    target = st.selectbox(
        'ターゲット言語',
        target_languages,
        label_visibility="collapsed"
    )

with row2_left:
    input = st.text_area(
        "入力テキスト",
        label_visibility="collapsed",
        height=200,
        placeholder="翻訳したい文章を入力してください"
    )

with row2_right:
    if input != "":
        with st.spinner("翻訳中..."):
            time.sleep(3)
            st.write("[ダミーメッセージ]")
