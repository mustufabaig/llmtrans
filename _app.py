import streamlit as st
import json

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
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


llm = AzureChatOpenAI(temperature=0, deployment_name=OPENAI_CHAT_MODEL, model='gpt-4', verbose=True)
res = llm([HumanMessage(content="Tell me a joke about a penguin sitting on a fridge.")])
st.write(res)
        
