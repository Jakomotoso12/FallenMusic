from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "23534271"))
API_HASH = getenv("API_HASH", "be4e91de58529a1b199b6d6515f2005e")
BOT_TOKEN = getenv("BOT_TOKEN", "5740372650:AAEms7wE6IFlhE6kwzvwTUABNK3qEbTnneM")
BOT_NAME = getenv("BOT_NAME","ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ")
BOT_USERNAME = getenv("BOT_USERNAME", "Pari_zmsic_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Ishq_ka_raja_143")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Ishq_ka_raja_143")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/038cfdb12f907f2f260ba.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/e4fc1d23ce6f3b0c9018c.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQB3_TCC7cNBnChSXIMo0tXsUHxkByr2lBAHThOHESIOtiJtJGj5M507HPky_EMGGesxOhz5o0LI-x5BuIs3TVnjMzE55YoubyQl4RWWYd2kbmUhKGS1iaspvPKaokzOiB_jaNWARlVmuFDZg41XYL5nd_nTTNuSqSDdoBmIfcVUIyRCDIDCslCCr5sp8HhCxuxfa7qKswiYYBPqeyTo92k8aR2qTYmkUCNzncj98eUaie2qhB_flWqw6HkkFwH42OGq6-OmmB9OHChaELifwNJEEY5LogrA__f8unfHZ6-fLVpbMwuPj4JuzMVEUZqR9JdlJ_ora_azAyrH994dkmD5AAAAAUESlZwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5565653587").split()))
