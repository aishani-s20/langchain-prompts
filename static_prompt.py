import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header('Reasearch Tool')

user_input = st.text_input('Enter name of research paper')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)