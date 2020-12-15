from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from freechatbot import settings

chatbot = ChatBot(**settings.CHATTERBOT)

# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train(
#                 "chatterbot.corpus.english",
#
#               )
# from chatterbot.trainers import ListTrainer
#
# trainer = ListTrainer(chatbot)
#
# trainer.train([
#     "How are you?",
#     "I am good.",
#     "That is good to hear.",
#     "Thank you",
#     "You are welcome.",
#     "What's your name?",
#     "My name is Chatterbot",
#     "know your name",
#     "My name is Chatterbot",
#     ])

from chatterbot.trainers import UbuntuCorpusTrainer


trainer = UbuntuCorpusTrainer(chatbot)

# Start by training our bot with the Ubuntu corpus data
trainer.train()