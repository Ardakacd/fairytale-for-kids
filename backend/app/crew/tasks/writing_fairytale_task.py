from textwrap import dedent
from crewai import Task

def writing_fairytale_task(
    prompt: str,
    text_analysis: str,
    image_analysis: str
):
    return Task(
        description=dedent(
            f"""
            **Task**: Write a Fairytale

            **Description**: Using the user's prompt and the provided analyses, craft an enchanting fairytale.
            Weave together the themes, emotions, characters, setting, conflict, resolution, and tone
            from **text_analysis**, along with the scene descriptions, objects, colors, mood, style,
            and actions from **image_analysis**. Structure the story into individual "pages."

            **Parameters**:
            - Prompt: {prompt}
            - Text Analysis: {text_analysis}
            - Image Analysis: {image_analysis}

            **Note**: Separate each page by a line of exactly nine hyphens (`---------`). 
            Do not include any extra commentary or JSON wrappers. Just create 2 page long fairytale.
            """
        ),
        expected_output="the fairytale separated by pages"
    )

