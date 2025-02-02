from langserve import add_routes
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate # To create a prompt
from langchain_core.output_parsers import StrOutputParser  # To manage the output in a structured way
import os # To access environment variables
import streamlit as st # To create a web application UI-UX for end to end project
import uvicorn # To run the FastAPI server
from fastapi import FastAPI # To create a FastAPI server
from dotenv import load_dotenv # To load environment variables from a .env file

# Load environment variables
load_dotenv()
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGSMITH_TRACING'] = os.getenv('LANGSMITH_TRACING')


# Creating the FastAPI server
app = FastAPI(
    title='LLM Model Comparison',
    description='Testing the performance of Deepseek against Gemma2 and Llama3.2',
    version='1.0.0'
)

# Deepseek LLM call
deepseek=Ollama(model='deepseek-r1:1.5b')
# Gemma LLM Model (Google Deepmind)
gemma= Ollama(model='gemma2:2b')
# Llama 3.2 LLM Model (Meta AI)
llama=Ollama(model="llama3.2:latest")
output_parser=StrOutputParser()   # Displays the output in string format


### Prompt making
prompt=ChatPromptTemplate([
    ('system','Test the performance of Deepseek model againt Gemma2 and Llama3.2'),
    ('user','Question: {question}')
])

add_routes(
    app,
    prompt|deepseek|output_parser,
    path="/deepseek"
)

add_routes(
    app,
    prompt|gemma|output_parser,
    path="/gemma"
)

add_routes(
    app,
    prompt|llama|output_parser,
    path="/llama"
)

if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8501)

