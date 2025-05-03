from textwrap import dedent
from crewai import Agent
from app.crew.constants import llm

def image_generator_agent():
   
    return Agent(
        role="Image Generation Agent",
        goal=(
            "Given a paged fairytale (pages separated by '---------'), "
            "generate a high-quality illustration for each page."
        ),
        backstory=(
            "You are an expert image generator. "
            "You take each page of a fairytale, write a concise prompt "
            "invoke an image-generation tool to create the actual image."
        ),
        llm=llm,
    )
