from textwrap import dedent
from crewai import Task

def generate_images_from_story_task(fairytale_text: str):
   
    return Task(
        description=dedent(
            f"""
            **Task**: Generate Fairytale Illustrations

            **Description**: Given the multi-page fairytale text, split it on the delimiter
                (`---------`) into individual pages. For each page, generate a high-quality illustration.

            **Parameters**:
            - Story (paged text):
            {fairytale_text}
            """
        ),
        expected_output="the image analysis for the text"
    )
