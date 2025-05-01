from textwrap import dedent
from crewai import Task

def understanding_image_task(image_urls: list[str]):
    """
    Creates a Task that:
      - Takes a list of image URLs (or file paths)
      - Analyzes each image to extract scene descriptions
      - Returns a JSON array of analysis objects, one per image
    """
    return Task(
        description=dedent(f"""
            **Task**: Image Understanding

            **Description**: Analyze the provided images and extract, for each one:
              - A high-level scene_description (what's happening and where)
              
            **Parameters**:
            - Images: {image_urls}

            **Instructions**:
            1. Use the Image Understanding Tool with the following images: {image_urls}
            2. The tool expects a list of image paths as input
            3. Process each image and return the scene descriptions
        """),
        expected_output="the image analysis as a json object",
    )
