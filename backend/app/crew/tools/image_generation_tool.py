from crewai.tools.base_tool import BaseTool
import torch
from diffusers import AmusedPipeline
import uuid
from pydantic import PrivateAttr

class ImageGenerationTool(BaseTool):
    """
    A tool that generate images from a fairytale.
    """
    name: str = "Image Generation Tool"
    description: str = "A tool that generates multiple images from a given fairytale. It returns the image paths."

    _pipe: AmusedPipeline = PrivateAttr()

    def __init__(self):
        super().__init__()
        self._pipe = AmusedPipeline.from_pretrained(
            "amused/amused-512", variant="fp16", torch_dtype=torch.float16
        )
    
    def _run(self, fairytale_text: str):
        """
        Generates images from a given fairytale
        """
        image_paths = []
        pages = str(fairytale_text).split("---------")
        
        for page in pages:
            if len(page.strip()) > 0:
                image = self._pipe(page.strip(), generator=torch.manual_seed(0)).images[0]
                id = str(uuid.uuid4())
                image_path = f"generated/{id}.png"
                image.save(image_path)
                image_paths.append(image_path)

        return image_paths

