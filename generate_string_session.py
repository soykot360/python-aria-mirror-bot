from pyrogram import Client

API_KEY = 1667813
API_HASH = "1f6921c27bf6cd01aba471a14ff33bcb"
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
