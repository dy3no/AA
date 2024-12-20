import re
import os
from os import environ
from pyrogram import enums
import asyncio
import json
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

API_ID = int(os.environ.get('API_ID', '27705761'))
API_HASH = os.environ.get('API_HASH', '822cb334ca4527a134aae97f9fe44fd6')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7688784612:AAG2i-qcDpxY3GNe7hdipfWCXToXW42kO2g')
PORT = os.environ.get("PORT", "8080")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6987158459').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002359661129'))

# for mongodb
DATABASE_NAME = os.environ.get("DB_NAME", "Cluster0")     
DATABASE_URI  = os.environ.get("DB_URL", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MONGO_URL = os.environ.get('MONGO_URL', "")



