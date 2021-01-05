from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from freechatbot import settings
import os, requests, sys, tarfile, glob, ntpath, csv
from sqlalchemy import create_engine
import pandas as pd

chatbot = ChatBot(**settings.CHATTERBOT)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
                "chatterbot.corpus.english",

              )
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
    "What's your name?",
    "My name is Chatterbot",
    "know your name",
    "My name is Chatterbot",
    ])

from chatterbot.trainers import UbuntuCorpusTrainer


# trainer = UbuntuCorpusTrainer(chatbot)

# Start by training our bot with the Ubuntu corpus data
# trainer.train()


class CustomUbuntuCorpusExtraxter:#(UbuntuCorpusTrainer):

    def download_file(self):
        url = 'http://cs.mcgill.ca/~jpineau/datasets/ubuntu-corpus-1.0/ubuntu_dialogs.tgz'
        file_path = './ubuntu_dialogs.tgz'
        show_status = True
        if os.path.exists(file_path):
            print('Downloaded')
            return True
        else:
            with open(file_path, 'wb') as open_file:
                print('Downloading %s' % url)
                response = requests.get(url, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None:
                    # No content length header
                    open_file.write(response.content)
                else:
                    download = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        download += len(data)
                        open_file.write(data)
                        if show_status:
                            done = int(50 * download / total_length)
                            sys.stdout.write('\r[%s%s]' % ('=' * done, ' ' * (50 - done)))
                            sys.stdout.flush()

                # Add a new line after the download bar
                sys.stdout.write('\n')

    def unzip(self):
        zip_file = './ubuntu_dialogs.tgz'
        file_path = './ubuntu_dialogs'
        if os.path.isdir(file_path):
            print('extracted')
            return True
        with tarfile.open(zip_file) as tar:
            tar.extractall('.')

    def get_data(self):
        def clean_up(txt):
            sp_char = {
                '"': '\\"'
            }
            for x in sp_char:
                txt = txt.replace(x,sp_char[x])
            return txt

        path = r'C:\Users\wongel\ubuntu_data\ubuntu_dialogs'
        corpus_path = os.path.join(
            path,
            'dialogs', '**', '*.tsv'
        )

        file_list = glob.glob(corpus_path)

        db = create_engine('sqlite:///text.sqlite3')
        cols = ['date','from','to','msg']


        for tsv_file in file_list:
            if '.tsv' in tsv_file[-4:]:
                print("reading {}".format(tsv_file))
                # df = pd.read_csv(tsv_file,
                #                  delimiter='\t',
                #                  header=None,
                #                  names=['date','from','to','msg'],
                #                  encoding='utf-8',
                #                  error_bad_lines=False
                #                  )
                df = pd.DataFrame(columns=cols)
                with open(tsv_file, 'r', encoding='utf-8') as tsv:
                    print("reading {}".format(tsv_file))
                    reader = csv.reader(tsv, delimiter='\t')

                    for row in reader:
                        if len(row) > 0:
                            df = df.append(pd.DataFrame([row],columns=cols))

                path,file_name = ntpath.split(tsv_file)
                df['file'] = "{}/{}".format(os.path.basename(path),file_name)
                df['date'] = pd.to_datetime(df['date'])
                # for col in df.columns:
                #     df[col] = df[col].apply(clean_up)
                df.to_sql('ubuntu_corpus',db,index=False, if_exists='append')
                os.rename(tsv_file,tsv_file.replace('.tsv','.tsv.done'))



# CustomUbuntuCorpusExtraxter().get_data()