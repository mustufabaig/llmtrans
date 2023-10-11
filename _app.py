import streamlit as st
import json

from langchain.chat_models import AzureChatOpenAI
from langchain import PromptTemplate

template = """Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "I don't know".

Context: Large Language Models (LLMs) are the latest models used in NLP.
Their superior performance over smaller models has made them incredibly
useful for developers building NLP enabled applications. These models
can be accessed via Hugging Face's `transformers` library, via OpenAI
using the `openai` library, and via Cohere using the `cohere` library.

Question: {query}

Answer: """

prompt_template = PromptTemplate(
    input_variables=["query"],
    template=template
)

st.code(
    prompt_template.format(
        query="Which libraries and model providers offer LLMs?"
    )
)

def get_chain():
    if 'chain' not in st.session_state:
        st.write('dbchain was not in the session')
        #loading config from streamlit settings
        OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
        OPENAI_API_BASE = st.secrets["OPENAI_API_BASE"]
        OPENAI_API_TYPE = st.secrets["OPENAI_API_TYPE"]
        OPENAI_API_VERSION = st.secrets["OPENAI_API_VERSION"]
        OPENAI_CHAT_MODEL = st.secrets["OPENAI_CHAT_MODEL"]
        
        # setup
        llm = AzureChatOpenAI(temperature=0, deployment_name=OPENAI_CHAT_MODEL, model='gpt-4', verbose=True)
        
        #prompt template
    
        local_chain = "I m local chain"
        st.session_state['txt_chain'] = local_chain
        return local_chain
        
    return st.session_state['chain']

chain = get_chain()
