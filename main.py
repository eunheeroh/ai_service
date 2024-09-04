# from dotenv import load_dotenv
import os
import streamlit as st
from langchain.llms import OpenAI

# Load environment variables
# load_dotenv()

# Initialize the OpenAI model
api_key = os.getenv('OPENAI_API_KEY')  # Make sure this environment variable is set in your .env file
llm = OpenAI(api_key=api_key)

st.title("동화 작가")

# Get input from the user
content = st.text_input('동화의 주제를 게시해주세요~')

# Generate poem when button is clicked
if st.button("동화주제 요청하기"):
    with st.spinner('동화 작성중....'):

    # Use the initialized llm to predict
        result = llm.predict(content + "에 대한 동화를 써줘")
        st.write(result)
