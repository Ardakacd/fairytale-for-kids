from app.crew.tasks.checking_fairytale import checking_fairytale_task
from app.crew.tasks.understanding_text_task import understanding_text_task
from app.crew.tasks.understanding_image_task import understanding_image_task
from app.crew.tasks.image_generation_task import image_generation_task
from app.crew.tasks.writing_fairytale_task import writing_fairytale_task

class FairyTaleTask:
 
    def understand_text(self, text: str):
        return understanding_text_task(text)
    
    def understand_image(self, image_urls: list[str]):
        return understanding_image_task(image_urls)
    
    def write_fairytale(self, prompt: str, text_analysis: str, image_analysis: str):
        return writing_fairytale_task(prompt=prompt, text_analysis=text_analysis, image_analysis=image_analysis)
    
    def generate_images(self, fairytale_text: str):
        return image_generation_task(fairytale_text)
    
    def check_fairytale(self, fairytale_text: str):
        return checking_fairytale_task(fairytale_text)
    
    
