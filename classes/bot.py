import logging
from twitchio.ext import commands
from classes.config import Config
from commons import helpers

class Bot(commands.Bot):

    def __init__(self) -> None:
        self.config = Config.parse_config('config.json')

        super().__init__(token=self.config.token, prefix=self.config.prefix, initial_channels=helpers.get_initial_channels(self.config))

    async def load_modules(self) -> None:
        module_folders = ["cogs"]
        for module in module_folders:
            for extension in helpers.list_module(module):
                curr_ext = helpers.split_file_ext(extension)
                try:
                    self.load_module(f'{module}.{curr_ext}')
                    logging.info(f"Loaded module {curr_ext}.")
                except Exception as e:
                    logging.warn(f"Failed to load module {module}.{curr_ext}. {e}")

    async def event_ready(self) -> None:
        logging.info(f"Bot is ready. We are connected as {self.nick}")
        await self.load_modules()
