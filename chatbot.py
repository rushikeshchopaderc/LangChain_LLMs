# from langchain_openai import ChatOpenAI # To extract/import a LLM model from OpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate # To create a prompt
from langchain_core.output_parsers import StrOutputParser  # To manage the output in a structured way
from dotenv import load_dotenv # To load environment variables from a .env file
import os # To access environment variables
import streamlit as st # To create a web application UI-UX for end to end project

# Load environment variables
load_dotenv()
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY') # not needed if you want to use the ollama opensource model
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
os.environ['LANGSMITH_TRACING'] = os.getenv('LANGSMITH_TRACING')


# Creating the chatbot
prompt=ChatPromptTemplate([
    ('system', 'Hi, Wanna test the new Deepseek model'),
    ('user','Question: {question}')
])

# Creating the web interface for the chatbot. Readymade due to streamlit library
st.title('Deepseek Chatbot Testing')
input_text=st.text_input('Enter the question to evaluate the performance of the Deepseek model')

# Deepseek LLM call
llm=Ollama(model='deepseek-r1:1.5b')
output_parser=StrOutputParser()   #Displays the output in string format

# Making a chain to interact in a structured way
chain=prompt | llm | output_parser

# Interacting with the chatbot whenever the input is provided
if input_text:
    st.write(chain.invoke({'question':input_text}))
