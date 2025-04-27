import os


class Settings():
    API_PREFIX: str = "/api"
    DEBUG: bool = os.getenv("DEBUG", False)
    PROJECT_NAME: str = "FairyAsle API"
    PROJECT_DESCRIPTION: str = "AI-Powered Fairytales for Kids"
    VERSION: str = "0.1.0"
    
    # Add other configuration settings as needed
    # DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    # SECRET_KEY: str = os.getenv("SECRET_KEY", "")

    class Config:
        env_file = ".env"

settings = Settings() 