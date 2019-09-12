import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

try:
    DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
except KeyError as e:
    raise KeyError("Environment {} is not found.\nPlease check that value.".format(e))