from pathlib import Path

import yaml

from src.logger import get_logger

logger = get_logger(__name__)

logger.info("Starting the applications")
logger.error("This is an error")


def read_config(config_path):
    config_path = Path(config_path)
    if not config_path.exists():
        logger.error(f"Config file not found at {config_path}")
        raise FileNotFoundError
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            return config
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file {config_path}: {e}")
        raise


if __name__ == "__main__":
    print("hi")
    config = read_config("config/config.yaml")
    print(config)
