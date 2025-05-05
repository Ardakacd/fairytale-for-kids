from textwrap import dedent
from crewai import Task

def generate_images_from_story_task(fairytale_text: str):
   
    return Task(
        description=dedent(
            f"""
            **Task**: Generate Fairytale Illustrations

            **Description**: Given the fairytale text, generate high-quality illustrations.
            The text contains page delimiters ('---------'). You must pass the ENTIRE text
            to the ImageGenerationTool, including all delimiters. Do not modify or remove any delimiters.

            **Parameters**:
            - Story: {fairytale_text}

            **Instructions**:
            1. Pass the ENTIRE fairytale text to the ImageGenerationTool, including all delimiters
            2. Do not modify or remove any delimiters from the text
            3. The tool will handle the page splitting and image generation internally
            4. It may take some time to generate the images but no need to worry
            5. Do not include any extra commentary or JSON wrappers. Just return the image paths as a list of strings.
            """
        ),
        expected_output="the generated image paths"
    )
