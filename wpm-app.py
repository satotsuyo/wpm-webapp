import streamlit as st

# タイトルを表示
st.title("WPM（Words Per Minute）測定アプリ")

# 読む英文を入力（サイズを調整するために st.text_area を使用）
text = st.text_area("読む英文を入力してください", height=200)  # heightを変更して高さを調整

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
