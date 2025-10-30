import streamlit as st
import os
from PIL import Image
from openai import OpenAI
if "messages" not in st.session_state:
    st.session_state.messages = []
image = Image.open(r"d:\Desktop\Sissi\o.jpg")
st.title(":streamlit: :rainbow[sissi] :streamlit:")
st.header("欢迎来到甄契智能AI",divider = "rainbow")
st.text_area("安全提示","请文明用语\n""不要违反法律")
st.sidebar.text("边栏")
st.sidebar.text_input("账号")
st.sidebar.text_input("密码")
qw = st.sidebar.button("提交",type = "primary")
st.sidebar.link_button("导航","https://www.baidu.com/")
bl = st.sidebar.radio("你觉得对你有帮助吗？",["有用","有点用","无用"],captions = ["值得鼓励","继续努力","需要提升"])
st.sidebar.write("你的选择是",bl)
st.snow()
st.image(image,"sissi")
if st.sidebar.button('清除历史记录'):
    st.session_state.messages = []
    st.rerun()
client = OpenAI(
    api_key="sk-caa08ff7e9c64786b45e9b98ec281ee1",
    base_url="https://api.deepseek.com")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
tiwenkuang = st.chat_input(placeholder = "请输入文字")
if tiwenkuang:
    st.session_state.messages.append({"role":"user","content":tiwenkuang})
    with st.chat_message("user"):
        st.write(tiwenkuang)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": tiwenkuang},
        ],
        stream=False
    )
    st.markdown(response.choices[0].message.content)
    st.session_state.messages.append({"role":"assistant","content":response.choices[0].message.content})
