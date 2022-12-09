import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "BQC1_5lUOFE-WPehztZU-6-QEBtKC6rUXQdXJhyLLANiVRJkUELDWUFJUTl3v9L5Eb7YnnawSGig2towh24M2hB8uJtUV4ykB7M7ljry1bh9vmbFgNsWd7OWl5CrVf3o0X3lCnLkfNwr1HNPUzA6-xZxJ5Glgi_lShwzHYC5JVZZTKnbuiMqISfkgIjQ1KOw7u29wKg67TCEZSzDZZ5u6YK7JK5_NnIEB-5XfW7krc574HtI8Ras6-cIMTEE2Q0COU3VzOXgO4z3MllSkAB4J_bOwR9SkgkO60Q8vFe-TwEgLGGJDPm-VfNUp-Lb5cw4B_5fy3LvzVsyyupVOIPd4nr0WID4aAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
