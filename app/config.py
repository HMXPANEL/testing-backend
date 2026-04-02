from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "AI Agent Brain"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # NVIDIA LLM Settings
    NVIDIA_API_KEY: str
    NVIDIA_BASE_URL: str = "https://integrate.api.nvidia.com/v1"
    NVIDIA_MODEL_NAME: str = "meta/llama3-70b-instruct"

    # Android WebSocket Secret
    ANDROID_WEBSOCKET_SECRET: str = "your_android_secret_key"

    # Database Settings
    SQLITE_DB_PATH: str = "./data/memory.db"
    CHROMA_DB_PATH: str = "./data/chroma_db"

    # Agent Settings
    MAX_AGENT_ITERATIONS: int = 15
    AGENT_LOOP_INTERVAL_SEC: int = 1

settings = Settings()
