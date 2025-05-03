from crewai import Agent
from app.crew.constants import llm
from app.crew.tools.understanding_image_tool import ImageUnderstandingTool
def image_understanding_agent():
    return Agent(
        role="Image Understanding Agent",
        goal=(
            "Analyze the input images and extract high-level scene descriptions."
        ),
        backstory=(
            "You are an image analysis assistant. For each image, you identify:\n"
            "  • scene_description: what's happening and where\n"
            "\n"
            "You have access to the Image Understanding Tool which takes a list of image paths as input.\n"
            "When using the tool, pass the list of image paths directly to it."
        ),
        llm=llm,
        tools=[ImageUnderstandingTool()],
        verbose=True
    )
