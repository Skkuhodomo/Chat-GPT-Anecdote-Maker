#from dotenv import load_dotenv
import streamlit as st

#load_dotenv()
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
st.title('인공지능 오늘의 한 마디.')
st.title('GPT가 꽤 괜찮은 한 마디를 작성합니다.  :sunglasses:')
content = st.text_input('주제 제시')

if st.button('한 마디 요청하기'):
    result = chat_model.predict(content +"에 관해 한 마디 해(10단어이내)")
    st.write(result)
    



