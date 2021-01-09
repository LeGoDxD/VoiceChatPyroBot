# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1555595
API_HASH = "6482c597a54f0f49d881401f0c16e71c"

# Get this from @Botfather
TOKEN = "1554977448:AAGqfAm3-6nfHHlouRFkHn1mz3Ov0Ahy3eo"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    383407735,
    951435494,
    1392620345
]

# The ID of the group where your bot streams
GROUP = False

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Send "now playing" messages to the group
LOG = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 10

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
