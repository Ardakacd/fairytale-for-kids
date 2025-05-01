from textwrap import dedent
from crewai import Task
from app.crew.agents.ImageUnderstandingAgent import image_understanding_agent

def understanding_image_task(image_urls: list[str]):
    """
    Creates a Task that:
      - Takes a list of image URLs (or file paths)
      - Analyzes each image to extract scene descriptions, objects, colors, mood, style, actions, and relationships
      - Returns a JSON array of analysis objects, one per image
    """
    return Task(
        description=dedent(f"""
            **Task**: Image Understanding

            **Description**: Analyze the provided images and extract, for each one:
              - A high-level scene_description (what's happening and where)
              - A list of objects with optional confidence scores
              - The dominant color palette
              - The overall mood/atmosphere
              - The artistic/photographic style
              - Any key actions or interactions (relationships)

            **Parameters**:
            - Images: {image_urls}
        """),
        expected_output="the image analysis as a json object"
    )
