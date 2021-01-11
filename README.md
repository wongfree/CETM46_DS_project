## Introduction
Project for CETM46 - chatbot
This project trying to implement a web-base ChatBot with Django & Chatterbot library. 


## Installation

* install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* install [python3](https://www.python.org/downloads/)
* Create and enable [Virtual Environment](https://docs.python.org/3/tutorial/venv.html) 
```bash
mkdir working_dir
cd working_dir
python -m venv venv
```
for windows system
```bash
venv\scripts\activate.bat
```
for Mac or Linux
```bash
source venv/bin/activate
```
* Clone the source code to your Local
```
git clone https://github.com/wongfree/CETM46_DS_project.git
```
* install the required library
```bash
cd CETM46_DS_project
pip3 install -r requirements.txt
```
* install required Spacy language pack
```bash
python -m spacy download en
``` 
* run the prototype server locally
```bash
python manage.py runserver
```
* access the prototype server at http://127.0.0.1:8000/


## With Full trained DB
in order to use full trained DB, you will need to modify the the train.py file as follow steps.,br/>
**this will cause the bot slow response<br/>
1st - uncomment following code at the bottom of train.py file:
```
trainer = UbuntuCorpusTrainer(chatbot)
# Download and training our bot with the Ubuntu corpus data
trainer.train()
```
2nd - run train.py:
```bash
python train.py
```


## Dataset:

Ubuntu CS log from McGill School of Computer Science <br/>
http://cs.mcgill.ca/~jpineau/datasets/ubuntu-corpus-1.0/ubuntu_dialogs.tgz<br/>

### Demo site host under Heroku
https://freechatbot.herokuapp.com/chatbot/ <br/>
<small><i> * because of the hosting limit the demo site only applied a simple trained model 

