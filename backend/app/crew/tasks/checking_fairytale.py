from textwrap import dedent
from crewai import Task

def checking_fairytale_task(fairytale_text: str):
    """
    Creates a Task that:
      - Takes a multi-page fairytale (pages delimited by exactly nine hyphens `---------`)
      - Sanitizes any language that could upset or confuse children
      - Preserves the original story flow, number of pages, and delimiters
    """
    return Task(
        description=dedent(f"""
            **Task**: Sanitize Fairytale Content

            **Description**: Review the provided multi-page fairytale text (pages separated by lines of exactly nine hyphens `---------`) 
            and replace or rephrase any words or phrases that could negatively affect children. Preserve the story's original flow, 
            structure, and page delimiters.

            **Parameters**:
            - Fairytale Text: {fairytale_text}
        """),
        expected_output="the sanitized fairytale text as a plain string"
    )
