from crewai.tools.base_tool import BaseTool
import base64
import uuid
from app.crew.constants import client
import re

class ImageGenerationTool(BaseTool):
    """
    A tool that generate images from a fairytale.
    """
    name: str = "Image Generation Tool"
    description: str = "A tool that generates multiple images from a given fairytale. It returns the image paths."
 
    def _run(self, fairytale_text: str):
        """
        Generates images from a given fairytale
        """
        image_paths = []
        pages = re.findall(r"<page>(.*?)</page>", fairytale_text, re.DOTALL)
        pages = [page.strip() for page in pages]
        
        for page in pages:
            if len(page.strip()) > 0:
                result = client.images.generate(
                    model="gpt-image-1",
                    prompt=page.strip(),
                    size="1024x1024"
                )
                
                id = str(uuid.uuid4())
                image_path = f"generated/{id}.png"
                
                image_base64 = result.data[0].b64_json
                image_bytes = base64.b64decode(image_base64)

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                image_paths.append(image_path)

        return image_paths

