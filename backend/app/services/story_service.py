import os
import uuid
from datetime import datetime
from typing import List, Optional
from fastapi import UploadFile
import asyncio
from app.models.story import Story, Page
from app.crew.flow import run_flow
# In-memory storage (replace with database in production)
stories = {}

async def create_story(prompt: str, images: Optional[List[UploadFile]] = None) -> Story:
    """
    Create a new story based on the prompt and optional images.
    In a real implementation, this would call AI services for story generation,
    image creation, and audio narration.
    """
    story_id = str(uuid.uuid4())
    
    image_paths = []
    if images:
        for i, img in enumerate(images):
            file_extension = os.path.splitext(img.filename)[1]
            file_path = f"uploads/images/{story_id}_{i}{file_extension}"
            
            with open(file_path, "wb") as f:
                f.write(await img.read())
            
            image_paths.append(file_path)
    
    # Placeholder for story generation (you'll implement the actual AI part)
    title = f"The Magical Adventure of {prompt.split()[0] if prompt else 'the Hero'}"

    flow_result =  await run_flow(prompt=prompt)

    pages = []

    for page in str(flow_result).split("---------"):
        if len(page) > 0:
            pages.append(Page(text=page, imageUrl=f"/api/images/{uuid.uuid4()}.jpg"))
     
    # Create the story object
    story = Story(
        id=story_id,
        title=title,
        prompt=prompt,
        pages=pages,
        createdAt=datetime.now()
    )
    
    # Store the story
    stories[story_id] = story
    
    return story

def get_story(story_id: str) -> Optional[Story]:
    """
    Retrieve a story by its ID.
    """
    return stories.get(story_id) 