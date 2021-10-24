import os
from classes.config import Config

def get_initial_channels(config: Config) -> list[str]:
    # For future use cases

    return config.initial_channels

def list_module(directory) -> list[str]:
    return (f for f in os.listdir(directory) if f.endswith('.py'))

def split_file_ext(filename) -> str:
    return os.path.splitext(filename)[0]
