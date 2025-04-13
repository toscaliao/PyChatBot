from chatterbot import ChatBot as b
import time
time.clock = time.time

chatbot = b(
    "ChatAI",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'     
              )