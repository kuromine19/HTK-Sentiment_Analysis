import streamlit as st
# import pytorch
import random as random
from transformers import pipeline
from preprocessing_text import cleanData


def to_sentiment(Sentiment):
    if Sentiment == 'LABEL_1':
        return 'Neutral'
    elif Sentiment == 'LABEL_2':
        return 'Positive'
    else:
        return 'Negative'


st.set_page_config(page_title="Sentiment Analysis")

# Tiêu đề trang web
st.title("Statistical Learning")
st.subheader("Final Semester Project")
st.subheader("Sentiment Analysis")

# Thông tin về thành viên trong nhóm
members = [
    {"name": "Tran Quoc Dinh", "MSSV": "20120056"},
    {"name": "Nguyen Tri Duc", "MSSV": "20120060"},
    {"name": "Nguyen Thanh Dat", "MSSV": "20120053"},
    {"name": "Tran Kim Bao", "MSSV": "20120041"}
]

# Biến để kiểm soát hiển thị thông tin thành viên
show_members = st.button("About Group")
if "show_member_info" not in st.session_state:
    st.session_state.show_member_info = False

# Hiển thị thông tin thành viên nếu biến cờ là True
if show_members:
    st.session_state.show_member_info = not st.session_state.show_member_info

if st.session_state.show_member_info:
    st.subheader("Team member information:")
    col1, col2 = st.columns(2)
    for i, member in enumerate(members):
        with col1 if i % 2 == 0 else col2:
            st.write(f"- **Full name:** {member['name']}")
            st.write(f"- **MSSV:** {member['MSSV']}")
            st.write("---")

# Tiêu đề nhập văn bản
st.header("Input Tweet")

# Ô input để nhập văn bản
context = st.text_area("Please type the tweet in the blank field")
context_processing=cleanData(context)

# Ô kết quả trả về đúng/sai
if st.button("Predict"):
    model_ckpt='../Model_saved'
    pipe=pipeline('sentiment-analysis',model=model_ckpt)
    st.write('Result: ', to_sentiment(pipe(context_processing)[0]['label']))
    st.write('Score: ', pipe(context_processing)[0]['score'])
