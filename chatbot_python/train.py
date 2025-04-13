'''
from chatterbot import ChatBot
import time
from yaml import *
time.clock = time.time
'''
from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")