from crewai import Task
from textwrap import dedent

def understand_text_task(text: str):
    return Task(
        description=dedent(
            f"""
            **Task**: Text Understanding

            **Description**: Analyze the input text to extract its core themes, emotional tones, 
            narrative elements (characters, setting, conflict, resolution), and overall tone/style.

            **Parameters**: 
            - Text: {text}
            """
        ),
        expected_output="the text analysis as a json object"
    )

