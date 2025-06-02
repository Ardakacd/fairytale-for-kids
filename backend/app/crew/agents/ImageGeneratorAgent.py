from crewai import Agent
from app.crew.constants import llm
from app.crew.tools.image_generation_tool import ImageGenerationTool
def image_generator_agent():
   
    return Agent(
        role="Image Generation Agent",
        goal=(
            "Given a fairytale text, "
            "generate high-quality illustrations."
        ),
        backstory=(
            "You are an expert image generator. "
            "You take a fairytale text, "
            "and pass the ENTIRE text to the ImageGenerationTool, including all delimiters. "
            "The tool will handle the page splitting internally. "
            "Do not modify or remove any delimiters from the text. "
            "Do not include any extra commentary or JSON wrappers. Just return the image paths as a list of strings."
        ),
        llm=llm,
        tools=[ImageGenerationTool()],
        verbose=True
    )
