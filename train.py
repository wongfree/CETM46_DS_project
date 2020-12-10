from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import en_core_web_sm
import spacy

nlp = spacy.load('en_core_web_sm')

chatbot = ChatBot('Chatterbot',
                  trainer='chatterbot.trainers.CorpusTrainer',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///db.sqlite3'
                  )
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
                "chatterbot.corpus.english",
                "chatterbot.corpus.english.greetings",
                "chatterbot.corpus.english.conversations"
              )