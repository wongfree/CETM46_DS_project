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
in order to link to full trained DB, you need to modify the the setting.py file, which located under: project/freechatbot/setting.py.<br/> 
*this will cause the bot slow response
chaneg following code:
```
line 149:   'database_uri':'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')),

-->

line 149:   'database_uri':'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db_full.sqlite3')),
```

## Dataset:

Ubuntu CS log from McGill School of Computer Science <br/>
http://cs.mcgill.ca/~jpineau/datasets/ubuntu-corpus-1.0/ubuntu_dialogs.tgz<br/>

### Demo site host under Heroku
https://freechatbot.herokuapp.com/chatbot/ <br/>
<small><i> * because of the hosting limit the demo site only applied a simple trained model 

