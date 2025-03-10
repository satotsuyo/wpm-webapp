import streamlit as st
import time

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

    # リーディングスタートボタンが押されたとき
    if st.button("リーディングスタート"):
        st.write("読み終わったら、終了ボタンを押してください")
        start_time = time.time()  # 開始時間を記録

    # 終了ボタンで時間を計測
    if 'start_time' in locals():  # start_timeが存在する場合のみ終了処理を行う
        if st.button("終了"):
            end_time = time.time()  # 終了時間を記録
            reading_time_s = end_time - start_time  # 経過時間を計算
            reading_time_m = reading_time_s / 60  # 分単位に変換

            # 読む時間が0だった時、再計測
            while reading_time_s == 0:
                st.write("読む時間が0秒です。再度計測してください")
                if st.button("リーディングスタート（再度）"):
                    start_time = time.time()
                if st.button("終了（再度）"):
                    end_time = time.time()
                    reading_time_s = end_time - start_time
                    reading_time_m = reading_time_s / 60

            # WPMを計算
            wpm = totalwords / reading_time_m

            # 結果を表示
            st.write(f"かかった時間は {round(reading_time_m, 2)} 分で")
            st.write(f"あなたのWPMは: {round(wpm, 2)} でした")
