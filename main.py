from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
def main():
    load_dotenv()
    chat_model = ChatOpenAI()
    st.title('AI Quote of the Day.')
    st.title('GPT comes up with a pretty cool quote. :sunglasses:')
    content = st.text_input('Topic suggestion')

    if st.button('Request a Quote'):
        result = chat_model.predict(content + " in 10 words or less")
        st.write(result)
if __name__ == 'main':
    main()


