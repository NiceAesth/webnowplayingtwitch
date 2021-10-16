import logging
from classes.bot import Bot

logging.basicConfig(level="INFO")

bot = Bot()

if __name__ == '__main__':
    try:
        bot.run()
    except KeyboardInterrupt:
        logging.info("Stopping bot.")