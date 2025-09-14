"""Configuration settings for CPE Innovation Framework"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Framework configuration settings"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
    
    # Framework Settings
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Network Settings
    NETWORK_TIMEOUT = int(os.getenv("NETWORK_TIMEOUT", "30"))
    MAX_DEVICES = int(os.getenv("MAX_CONCURRENT_DEVICES", "10"))
    
    # Analysis Settings
    PREDICTION_THRESHOLD = float(os.getenv("MAINTENANCE_PREDICTION_THRESHOLD", "0.7"))
    DEPLOYMENT_TIMEOUT = int(os.getenv("DEPLOYMENT_TIMEOUT", "300"))
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required")
        return True