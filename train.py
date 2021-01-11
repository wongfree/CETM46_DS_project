from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.trainers import ListTrainer
from freechatbot import settings

chatbot = ChatBot(**settings.CHATTERBOT)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
                "chatterbot.corpus.english.conversations",
                "chatterbot.corpus.english.emotion",
                "chatterbot.corpus.english.greetings",
                "chatterbot.corpus.english.food",
                "chatterbot.corpus.english.ai"
              )


trainer = ListTrainer(chatbot)

trainer.train([
        "How are you?",
        "I am good.",
        "That is good to hear.",
        "Thank you",
        "You are welcome.",
        "What's your name?",
        "My name is Freechatbot",
        "know your name",
        "My name is Freechatbot",
        ])

trainer.train([
    "Hello",
    "Hello, How can I help you",
    "My PC dead",
    "Sorry, i Can't understand clearly, Can you further explain the symptom?",
])

trainer.train([
    "Hi",
    "Hello, How can I help you",
    "My PC not working",
    "Sorry, i Can't understand clearly, Can you further explain the symptom?",
])

trainer.train([
    "Hi",
    "Hello, How can I help you",
    "My PC not working",
    "Sorry, i Can't understand clearly, Can you further explain the symptom?",
    "When i tried to open my excel, then it friezed",
    "Have you try restart your machine?",
    "Ok, let me try.",
    "Anything else i can help?"
])

trainer.train([
    "My program keep crashing",
    "Which program you talking?",
    "GIMP",
    "Have you try restart your machine?",
    "Yes, still same",
    "Could you provide which version of the program your using?",
    "2.1.1",
    "Have you try update your program version?",
    "Ok, let me try.",
    "Anything else i can help?",
    "No Thanks",
    "Thank you very much for using ur services."
])


# if want to train with Ubuntu corpus data, uncomment following part
# please be aware this process may take more then a days, depend on your computer performance

# trainer = UbuntuCorpusTrainer(chatbot)
#
# # Start by training our bot with the Ubuntu corpus data
# trainer.train()