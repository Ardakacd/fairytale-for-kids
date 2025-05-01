from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = "gpt-3.5-turbo"

llm = ChatOpenAI(
            model_name=MODEL_NAME, temperature=0.7)
