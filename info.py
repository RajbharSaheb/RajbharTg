# Copyright (C) 2023 DX-MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

import re
import time
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")
UPTIME = time.time()
PORT = int(environ.get("PORT", "8080"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "120"))
PING_WEB = environ.get("PING_WEB", "")
WEBHOOK = bool(environ.get("WEBHOOK", True))
MAINTENANCE_MODE = bool(environ.get("MAINTENANCE_MODE", False))
PREFIX = environ.get("PREFIX", "/")
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/9dbd024664e2b558cc988.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/eb0ab2892ea56608540e5.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/6f55d902f9bf2d0afd4bb.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/c72b425ebcb0858f735bc.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5838674798 5570163408').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001505492751').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5838674798 5570163408').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '5570163408').split()]
auth_channel = environ.get('AUTH_CHANNEL','')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'moneykamalo.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '8a04025f212aa7c29f79bb1c2ac28300e149a7e0')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
RemoveBG_API = environ.get("RemoveBG_API", "")
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/searchmoviesname')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/movies_island8')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Searchmoviesname/58779')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001930913574'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'rajbharmvsupport')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
PMFILTER = is_enabled((environ.get('PMFILTER', "False")), False)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
