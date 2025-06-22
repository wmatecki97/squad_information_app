from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or a .env file.
    """

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_nested_delimiter="__"
    )

    # LLM Settings - Using a model known for speed and excellent JSON output
    model_name: str = Field(default="google/gemini-2.5-flash")
    openrouter_api_key: str = Field(
        ...,
        description="Your OpenRouter API key. Must be set in .env file.",
    )

    # Football API Settings
    football_api_key: str = Field(
        ...,
        description="Your api-sports.io Football API key. Must be set in .env file.",
    )
    football_api_host: str = Field(default="v3.football.api-sports.io")

    is_trial_football_api_key: bool = Field(
        default=False,
        description="Set to True if using a trial API key with limited requests.",
    )
    
settings = Settings()