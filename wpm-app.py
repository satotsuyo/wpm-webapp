<<<<<<< HEAD
import streamlit as st
import time

# タイトルを表示
st.title("WPM（Words Per Minute）測定アプリ")

# 読む英文を入力
text = st.text_input("読む英文を入力してください")

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

    start_time = None  # start_timeの初期化

    # 読む時間を取得
    if st.button("リーディングスタート"):
        st.write("読み終わったら、終了ボタンを押してください")
        start_time = time.time()

    if st.button("終了") and start_time is not None:
        end_time = time.time()
        reading_time_s = end_time - start_time
        reading_time_m = float(reading_time_s / 60)

        # 読む時間が0だった時、再計測
        while reading_time_s == 0:
            st.write("読む時間が0秒です。再度計測してください")
            if st.button("リーディングスタート（再度）"):
                start_time = time.time()
            if st.button("終了（再度）"):
                end_time = time.time()
                reading_time_s = end_time - start_time
                reading_time_m = float(reading_time_s / 60)

        # WPMを計算
        wpm = totalwords / reading_time_m

        # 結果を表示
        st.write(f"かかった時間は {round(reading_time_m, 2)} 分で")
        st.write(f"あなたのWPMは: {round(wpm, 2)} でした")
=======
import streamlit as st
import time

# タイトルを表示
st.title("WPM（Words Per Minute）測定アプリ")

# 読む英文を入力
text = st.text_input("読む英文を入力してください")

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

    start_time = None  # start_timeの初期化

    # 読む時間を取得
    if st.button("リーディングスタート"):
        st.write("読み終わったら、終了ボタンを押してください")
        start_time = time.time()

    if st.button("終了") and start_time is not None:
        end_time = time.time()
        reading_time_s = end_time - start_time
        reading_time_m = float(reading_time_s / 60)

        # 読む時間が0だった時、再計測
        while reading_time_s == 0:
            st.write("読む時間が0秒です。再度計測してください")
            if st.button("リーディングスタート（再度）"):
                start_time = time.time()
            if st.button("終了（再度）"):
                end_time = time.time()
                reading_time_s = end_time - start_time
                reading_time_m = float(reading_time_s / 60)

        # WPMを計算
        wpm = totalwords / reading_time_m

        # 結果を表示
        st.write(f"かかった時間は {round(reading_time_m, 2)} 分で")
        st.write(f"あなたのWPMは: {round(wpm, 2)} でした")
>>>>>>> 6a5a746c613f7186cc0bcb020510abaadbdf92cc
