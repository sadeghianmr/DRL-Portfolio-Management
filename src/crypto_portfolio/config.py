from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Loads and validates settings from the .env file.
    """
    
    # This tells pydantic to look for a .env file
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8"
    )

    # These variables MUST match the names in your .env file
    database_url: str
    cryptocompare_api_key: str

@lru_cache()
def get_settings() -> Settings:
    """
    Returns a cached instance of the Settings object.
    Using lru_cache ensures the .env file is only read once.
    """
    return Settings()

# Create a single, importable instance for the rest of your app
settings = get_settings()


# --- To test this file ---
# You can run this file directly from your terminal to 
# check if it's loading your .env file correctly.
if __name__ == "__main__":
    print("Loading settings...")
    try:
        settings = get_settings()
        print("Settings loaded successfully!")
        print(f"Database URL: ...{settings.database_url[-10:]}") # Show last 10 chars
        print(f"CryptoCompare API Key: ...{settings.cryptocompare_api_key[-6:]}") # Show last 6 chars
    except Exception as e:
        print(f"Error loading settings: {e}")