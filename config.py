import os

class Config:
    API_ID = int(os.getenv("API_ID", 22141398))
    API_HASH = os.getenv("API_HASH", '0c8f8bd171e05e42d6f6e5a6f4305389')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '8105194942:AAF6tBo_Zf8st3LwxFL-sEfdmAbq7vIx-XY')
