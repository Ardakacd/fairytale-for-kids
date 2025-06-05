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
            **Task**: Write a Child-Friendly Fairytale

            **Description**: Create a magical, gentle fairytale for children aged 3–6. 
            Use the user's prompt, along with insights from the **text_analysis** 
            (themes, emotions, characters, setting, conflict, resolution, tone) 
            and **image_analysis** (scene descriptions, objects, colors, mood, style, actions).

            Write the story in simple, age-appropriate language. Avoid complex words, scary themes, or violence. 
            Make the story imaginative, comforting, and easy to read aloud — like a picture book or bedtime story.

            Structure the story into ** pages**, each short and self-contained, but part of a flowing story.

            **Parameters**:
            - Prompt: {prompt}
            - Text Analysis: {text_analysis}
            - Image Analysis: {image_analysis}

            **Note**:
            - Keep sentences short and vocabulary simple.
            - Use a warm, friendly tone.
            - Wrap each story page in `<page>` and `</page>` tags.
            - Output ONLY the fairytale — no commentary or JSON.
            """
        ),
        expected_output="A 2-page fairytale separated by `<page>` and `</page>` tags using simple, child-appropriate language"
    )
