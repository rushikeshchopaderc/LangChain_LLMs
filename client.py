import streamlit as st  # To create a web application UI-UX for end to end project
import requests
import os
from dotenv import load_dotenv # To load environment variables from a .env file

# Load environment variables - Will help in tracking the models on Langsmith
load_dotenv()
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGSMITH_TRACING'] = os.getenv('LANGSMITH_TRACING')


def get_response(prompt,path):
    response = requests.post('http://localhost:8501'+path+'/invoke', json={'input':prompt})
    return response.json()

# streamlit framework
st.title('LLM Model Comparison')
prompt=st.text_input('Test the performance of Deepseek model againt Gemma2 and Llama3.2')

if prompt:
    st.write(get_response(prompt, '/deepseek'))
    st.write(get_response(prompt,'/gemma'))
    st.write(get_response(prompt,'/llama'))


