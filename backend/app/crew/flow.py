from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from app.crew.tasks.understanding_text_task import understand_text_task
from app.crew.tasks.understanding_image_task import understanding_image_task
from app.crew.agents.TextUnderstandingAgent import text_understanding_agent
from app.crew.agents.ImageUnderstandingAgent import image_understanding_agent
from app.crew.tasks.writing_fairytale_task import writing_fairytale_task
from app.crew.agents.FairytaleTextWriterAgent import fairytale_text_writer_agent
from app.crew.tasks.image_generation_task import generate_images_from_story_task
from app.crew.agents.ImageGeneratorAgent import image_generator_agent



class FairyTaleState(BaseModel):
    prompt: str = ""
    fairytale_images: list[str] = []
    fairytale_text: str = ""
    fairytale_text_analysis: str = ""
    fairytale_image_analysis: str = ""


class FairyTaleFlow(Flow[FairyTaleState]):

    @start()
    def analyze_text(self):
        task = understand_text_task(self.state.prompt)
        agent = text_understanding_agent()
        result = agent.kickoff(task.description)
        self.state.fairytale_text_analysis = result

    @listen(analyze_text)
    def analyze_image(self):
        if self.state.fairytale_images:
            task = understanding_image_task(self.state.fairytale_images)
            agent = image_understanding_agent()
            result = agent.kickoff(task.description)
            self.state.fairytale_image_analysis = result

    @listen(analyze_image)
    def write_fairytale(self):
        task = writing_fairytale_task(self.state.prompt, self.state.fairytale_text_analysis, self.state.fairytale_image_analysis)
        agent = fairytale_text_writer_agent()
        result = agent.kickoff(task.description)
        self.state.fairytale_text = result

    @listen(write_fairytale)
    def generate_images(self):
        task = generate_images_from_story_task(self.state.fairytale_text)
        agent = image_generator_agent()
        result = agent.kickoff(task.description)
        self.state.fairytale_images = result
        return {
            "text": self.state.fairytale_text,
            "images": self.state.fairytale_images
        }
    

async def run_flow(prompt: str, fairytale_images: list[str]):
    flow = FairyTaleFlow()
    result = await flow.kickoff_async(inputs={"prompt": prompt, "fairytale_images": fairytale_images})
    return result




