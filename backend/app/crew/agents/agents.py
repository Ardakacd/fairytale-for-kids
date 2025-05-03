
from app.crew.agents.TextUnderstandingAgent import text_understanding_agent
from app.crew.agents.ImageUnderstandingAgent import image_understanding_agent
from backend.app.crew.agents.FairytaleTextWriterAgent import fairytale_writer_agent
from app.crew.agents.FairytaleCheckerAgent import fairytale_checker_agent

class FairyTaleAgents:
    def __init__(self):
        self.text_understanding_agent = text_understanding_agent()
        self.image_understanding_agent = image_understanding_agent()
        self.fairytale_writer_agent = fairytale_writer_agent()
        self.fairytale_checker_agent = fairytale_checker_agent()

