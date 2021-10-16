import os, json
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    """Class for storing the configuration info for the bot"""
    token: str
    prefix: str
    initial_channels: list[str]

    @classmethod
    def parse_config(self, path: str) -> "Config":

        if not os.path.exists(path):
            raise FileNotFoundError("Provided path is invalid.")
        
        with open(path, 'r') as config_json:
            config_data = config_json.read()
        config_dict = json.loads(config_data)

        return self(**config_dict)
