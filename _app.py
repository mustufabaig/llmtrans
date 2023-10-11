import streamlit as st
import json

from langchain.chat_models import AzureChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts.prompt import PromptTemplate
from langchain import FewShotPromptTemplate

import fewshotprompttemplate

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
        # now create the few shot prompt template
        few_shot_prompt_template = FewShotPromptTemplate(
            examples=fewshotprompttemplate.examples,
            example_prompt=fewshotprompttemplate.example_prompt,
            prefix=fewshotprompttemplate.prefix,
            suffix=fewshotprompttemplate.suffix,
            input_variables=["input", "table_info", "dialect"],
            example_separator="\n\n"
        )

        local_chain = "I m local chain"
        st.session_state['txt_chain'] = local_chain
        return local_chain
        
    return st.session_state['chain']

chain = get_chain()
