from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "AQJFh3kADlnaMC5sr5LYgz6tOXjs8TkEr5pB7pBVlXvNqXOUPzJDQDHDvg_Fkgp4Bwq73g4KeSZvfkhw4HQqGKA69XhBKtFYEG0kfr7IlZhaWYAYThSCWEri_s87TIbQGwI9y8mMWSCoOyvJ-NKFo1U4Zs-LOdCHGus7DUQaZxsy1QnUmh2LtHcZ8EpqmYbCxyPOuCU-5-EZKLr6jJRVpNK53Xmjea-NTTlKMeCxhS1KwROmDAkuHYcnqXB5Fvv7xJ0EEhoT6ceg79oeUVOai5Su7E22eEPwkO_qf5WB7vNJJyBpKedv_MEhBcAc6CwdrOEZePentAWnsEHFtMDDjisyy0wcqAAAAAH06w7uAA")
BOT_TOKEN = getenv("BOT_TOKEN" , "8501454605:AAGeInRoYLvdk4iGNWfyiAWE3ZfV-a0Gius")
API_ID = int(getenv("API_ID", "38111097"))
API_HASH = getenv("API_HASH" , "2a5c91155e981e849681f8f3e817d545")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI" , "ASbia6aQ0OJi3eeg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6022106985").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "8331571396").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "5165708730"))
MUSIC_BOT_NAME = getenv("LUCKY_MUSIC")
if str(getenv("SUPPORT_CHANNEL")).strip() == "https://t.me/AboutS4RKAR":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "https://t.me/Little_community":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
