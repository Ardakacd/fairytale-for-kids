from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from crewai.tools.base_tool import BaseTool
from pydantic import PrivateAttr


class ImageUnderstandingTool(BaseTool):
    """
    A tool that understands a list of images and returns scene descriptions.
    """
    name: str = "Image Understanding Tool"
    description: str = "A tool that analyzes images(given by list of paths) and provides scene descriptions."

    _processor: BlipProcessor = PrivateAttr()
    _model: BlipForConditionalGeneration = PrivateAttr()

    def __init__(self):
        super().__init__()
        self._processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self._model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self._model.to("cuda" if torch.cuda.is_available() else "cpu")

    def _run(self, images: list[str]) -> str:
        """
        Understand a list of images (given by paths) and return scene descriptions as a string.
        """
            
        scene_descriptions = ""
        
        
        for img_path in images:
            img = Image.open(img_path).convert("RGB")
            inputs = self._processor(images=img, return_tensors="pt").to(self._model.device)
            out = self._model.generate(**inputs, max_new_tokens=50)
            caption = self._processor.decode(out[0], skip_special_tokens=True)
            print("Caption:", caption)
            scene_descriptions += f"{caption}\n"

        return scene_descriptions.strip()
