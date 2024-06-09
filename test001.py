import streamlit as st
import pandas as pd

st.write("Hello World")

st.write("Hello :blue[World]")

st.title("Hello Wrold")

st.title("Hello Wrold :sunglasses:")

st.title("Hello Wrold :shit:")

st.write(
    pd.DataFrame(
        {
            "first":[1,2,3,4,5],
            "first":[1,2,3,4,5]
        }
    )
)

st.link_button("click here", "https://cae.over-field.com/")

st.header("Hello World", divider="rainbow")

code = """

st.title("Hello Wrold")

st.title("Hello Wrold :sunglasses:")

st.title("Hello Wrold :shit:")

st.write(
    pd.DataFrame(
        {
            "first":[1,2,3,4,5],
            "first":[1,2,3,4,5]
        }
    )
)
"""

st.code(code, language="Python")

agree = st.checkbox("I agree")

if agree:
    st.write("OK")

options = st.multiselect(
    "好きな色は何ですか？",
    ["赤", "緑", "青"]
)

st.write("あなたが選んだ色は：",options)

options = st.radio(
    "好きな色は何ですか？",
    ["赤", "緑", "青"]
)

st.write("あなたが選んだ色は：",options)

df = pd.DataFrame(
    [
        {"colors":"赤", "rating":4},
        {"colors":"緑", "rating":3},
        {"colors":"青", "rating":2}
    ]
)

editor_df = st.data_editor(df)
st.write(editor_df.loc[editor_df["rating"].idxmax()])
st.write(editor_df.loc[editor_df["rating"].idxmax()]["colors"])

df = pd.DataFrame(
    [
        {"colors":"赤", "rating":4, "mark":True},
        {"colors":"緑", "rating":3, "mark":False},
        {"colors":"青", "rating":2, "mark":True}
    ]
)

editor_df = st.data_editor(df)
editor_df = editor_df[editor_df["mark"]==True]
st.write(editor_df.loc[editor_df["rating"].idxmax()]["colors"])

# ダウンロードボタン
csv = editor_df.to_csv().encode("utf-8")
st.download_button(
    label="csvダウンロード",
    data=csv,
    file_name="sample_df.csv",
    mime="text/csv"
)

df = pd.DataFrame(
    {
        "sales":[20,30,50,70],
        "progress_sales":[200,300,400,500]
    }
)

st.data_editor(
    df,
    column_config={
        "progress_sales":st.column_config.ProgressColumn(
            min_value=0,
            max_value=500
        )
    }
)

df = pd.DataFrame(
    {
        "sales":[
            [20,30,50,70,100],
            [20,100,50,70,100]
            ],
    }
)

st.data_editor(df)

st.data_editor(
    df,
    column_config={
        "sales":st.column_config.BarChartColumn(
            y_min=0,
            y_max=100
        )
    }
)
st.data_editor(
    df,
    column_config={
        "sales":st.column_config.LineChartColumn(
            y_min=0,
            y_max=100
        )
    }
)

age = st.slider("あなたは何歳ですか？", 0, 120, 40)
st.write("私は", age, "歳です")

import datetime

date = st.date_input("あなたが生まれたのはいつですか？", datetime.date(2000,12,25))
st.write("私は",date, "に生まれました")

text = st.text_input("入力してください", "XXXXX")
st.write(text)

col1, col2 = st.columns(2)
with col1:
    st.title("Column1")
    st.write("カラム1")
with col2:
    st.title("Column2")
    st.write("カラム2")

tab1, tab2 = st.tabs(["tab1", "tab2"])
with tab1:
    st.title("Tab1")
    st.write("カラム1")
with tab2:
    st.title("Tab2")
    st.write("カラム2")

with st.expander("もっと詳しく見る") :
    st.write(code)

with st.popover("ポップアップ"):
    st.write(code)

with st.sidebar:
    st.write("testtetste")
    st.write("testtetste")

agree = st.checkbox("同意しますか？")
if agree:
    st.toast("Tank you", icon="👍")

birthday = st.checkbox("今日はあなたの誕生日ですか？")
# birthday = datetime.datetime.today()
if birthday:
    st.write(birthday)
    st.balloons()

# 複数ページ実装
st.page_link("test001.py", label="Home", icon="👍")
st.page_link("pages/test1.py", label="test1", icon="👍")
st.page_link("pages/test2.py", label="test2", icon="👍")
st.page_link("pages/test3.py", label="test3", icon="👍")
st.page_link("https://cae.over-field.com/", label="計算力学技術者資格アプリ")