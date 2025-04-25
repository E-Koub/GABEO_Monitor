import os
import yaml
import logging
import logging.config
from dotenv import load_dotenv

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.join(os.path.dirname(__file__), 'vendor'))

def setup_logging(logging_config_path="config/logging.yaml"):
    try:
        os.makedirs("logs", exist_ok=True)
        with open(logging_config_path, "r") as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)

    except Exception as e:
        print(f"[LOGGING ERROR] Failed to load logging config: {e}")
        logging.basicConfig(level=logging.DEBUG)  # fallback minimal


def create_context():
    load_dotenv()
    env = os.getenv("APP_ENV", "development")
    debug = os.getenv("APP_DEBUG", "True") == "True"

    setup_logging()
    logger = logging.getLogger("dataHive")
    logger.debug("Logger initialized with config/logging.yaml")

    settings = {}
    try:
        with open("config/settings.yaml", "r") as f:
            settings = yaml.safe_load(f)
    except FileNotFoundError:
        logger.warning("settings.yaml not found")

    return {
        "env": env,
        "debug": debug,
        "settings": settings,
        "logger": logger
    }
