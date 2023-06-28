from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "26016754"))
API_HASH = getenv("API_HASH", "a3016f81b79531612dcaf8a40bf8b546")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "5268653948"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "THECRAZYFRIENDS")
UPDATE_CHNL = getenv("UPDATE_CHNL", "THELEGENDGIRL")
OWNER_USERNAME = getenv("OWNER_USERNAME", "LUCIFER_OP1")

# Random Start Images
IMG = [
    "https://graph.org/file/d68cc5629ac666a37ebb6.jpg",
    "https://graph.org/file/be86c865e2f2f2755c2d1.jpg",
    "https://graph.org/file/77ac785e89aa404fe5288.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAxkBAAEJgptkm_m4_c0-Ne7R4ibtZWc5VxwAAYkAAicEAAJXomFUVo1nG4F49vcvBA",
    "CAACAgUAAxkBAAJSd2Sb-p-TaTQ8kSrLP_2H5KUduogRAAIhAQAC8mVYMxYetsudRvZdLwQ",
    "CAACAgUAAxkBAAJSc2Sb-ocRJARJN7IMKYETnCBORCdWAALYAQAC8mVYMz9DkjKVky2aLwQ",
]


EMOJIOS = [
    "🔪",
    "🕉",
    "💸",
    "🔥",
    "🥂",
    "🖤",
    "🍷",
    "🥀",
    "💀",
    "⚡",
]
