import streamlit as st
import json

from langchain.chat_models import AzureChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts.prompt import PromptTemplate
from langchain import FewShotPromptTemplate

import fewshotprompttemplate

