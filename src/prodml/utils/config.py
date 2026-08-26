from pathlib import Path
from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "ProdML Service"
    VERSION: str = "0.1.0"
    DEBUG: bool = False

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    DATA_RAW_DIR: Path = DATA_DIR / "raw" 
    DATA_RAW_DIR_FILE1: Path=DATA_RAW_DIR/ "iris.csv"   
    MODELS_DIR: Path = BASE_DIR / "models"
    LOGS_DIR: Path = BASE_DIR / "logs"

    TARGET_COL: str = "target"
    MODEL_NAME: str = "random_forest_v1.joblib"
    TEST_SIZE: float=0.2
    RANDOM_STATE: int = 42
    N_ESTIMATORS: int = 25
    MAX_DEPTH: int = 2

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  
    )


settings = Settings()

settings.DATA_DIR.mkdir(parents=True, exist_ok=True)
settings.DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)
settings.MODELS_DIR.mkdir(parents=True, exist_ok=True)
settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)