from chatterbot import ChatBot as b
import time
time.clock = time.time

bot = b(
    "ChatAI",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'     
              )

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"{bot.get_response(query)}")
