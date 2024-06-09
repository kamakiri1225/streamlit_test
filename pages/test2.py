import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

st.title("test2")
st.page_link("test001.py", label="Home", icon="👍")

st.title("Irisのデータを用いた予測アプリ")

iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="species")
st.write(iris.feature_names)

st.write(x)
st.write(y)

# 学習データとテストデータに分ける
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

# テストデータの予測
y_pred = model.predict(x_test)
accuracy_score = accuracy_score(y_test, y_pred)
st.write(f"精度は：{accuracy_score}")

# ユーザーが入下項目
st.header("好きな値を入力してください")
sepal_length = st.number_input("sepal length (cm)", min_value=0, value=3)
sepal_width = st.number_input("sepal width (cm)", min_value=0, value=3)
petal_length = st.number_input("petal length (cm)", min_value=0, value=3)
petal_width = st.number_input("petal width (cm)", min_value=0, value=3)

input_data = pd.DataFrame(
    {
        "sepal length (cm)": [sepal_length],
        "sepal width (cm)": [sepal_width],
        "petal length (cm)": [petal_length],
        "petal width (cm)": [petal_width]
    }
)

st.write(input_data)

if st.button("Predict"):
    prediction = model.predict(input_data)
    prediction_probes = model.predict_proba(input_data)
    st.write(prediction)
    st.write("各項目の確率")
    st.write(prediction_probes)
    species = iris.target_names[prediction][0]
    st.write(f"予測した品種は{species}です。")

st.header("データの可視化")
fig, ax = plt.subplots()
scatter = ax.scatter(x["petal length (cm)"], x["petal width (cm)"], c=y, label=iris.target_names)
ax.scatter(petal_length, petal_width,c="red")
ax.set_xlabel("petal length (cm)")
ax.set_ylabel("petal width (cm)")
hanrei, _ = scatter.legend_elements(prop="colors")
legend_labels = iris.target_names
ax.legend(hanrei, legend_labels, title="species")
st.pyplot(fig)