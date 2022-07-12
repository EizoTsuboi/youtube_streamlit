import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!!"

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

col1, col2 = st.columns(2)
button = col1.button("右カラムにボタンを表示")
if button:
    col2.write("ここは右からむ")

# option = col1.selectbox(
#     "あなたが好きな数字を教えてください",
#     list(range(1, 11))
# )
# col1.write("あなたの好きな数字は、", option, "です。")


# text = col2.sidebar.text_input("あなたの好きな数字は")
# value = st.sidebar.slider("好きな数字は", 0, 100, 50)

# col2.write("あなたの好きな数字は、", text, "です。")
# "あなたの好きな数字は、", value, "です。"

# if st.checkbox("Show Image"):
#     img = Image.open("/Users/eizo/Desktop/untitled.png")
#     st.image(img, caption="title", use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )


# st.map(df)
 # st.dataframe(df.style.highlight_max(axis=0))

