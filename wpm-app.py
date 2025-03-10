import streamlit as st

# タイトルを表示
st.title("WPM（Words Per Minute）測定アプリ")

# 読む英文を入力（keyを指定してIDの重複を避ける）
text = st.text_input("読む英文を入力してください", key="text_input_1")

if text:
    # 単語を区切る
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace('"', '')  # ダブルクォーテーションを削除
    text = text.replace('\'', '')  # アポストロフィも削除

    # 単語を区切る
    words = text.split()

    # 総語数をカウント
    totalwords = len(words)

    # 総語数を表示
    st.write(f"これから読む英文の総語数は {totalwords} です")
