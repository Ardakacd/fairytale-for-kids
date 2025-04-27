from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from typing import List, Optional
import os

from app.models.story import Story
from app.services.story_service import create_story, get_story

router = APIRouter(prefix="/api")

@router.post("/stories", response_model=Story)
async def create_story_route(
    prompt: str = Form(...),
    images: Optional[List[UploadFile]] = File(None)
):
    return await create_story(prompt, images)

@router.get("/stories/{story_id}", response_model=Story)
async def get_story_route(story_id: str):
    story = get_story(story_id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    
    return story

@router.get("/stories/{story_id}/pdf")
async def get_story_pdf(story_id: str):
    story = get_story(story_id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    pdf_path = "generated/pdfs/placeholder.pdf"
    
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"fairytale-{story_id}.pdf"
    )

@router.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = f"generated/images/{image_name}"
    
    if not os.path.exists(image_path):
        image_path = "generated/images/default.jpg"
    
    return FileResponse(image_path)

@router.get("/audio/{audio_name}")
async def get_audio(audio_name: str):
    audio_path = f"generated/audio/{audio_name}"
    
    if not os.path.exists(audio_path):
        audio_path = "generated/audio/default.mp3"
    
    return FileResponse(audio_path) 