import os, glob, time, csv, traceback
from dateutil.parser._parser import parse
import pandas as pd
from chatterbot.conversation import Statement
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.tagging import PosLemmaTagger
from chatterbot import languages, ChatBot



class myTrainer(UbuntuCorpusTrainer):

    def __init__(self,**kwargs):
        super().__init__(UbuntuCorpusTrainer, **kwargs)

    path = r'C:\Users\wongel\ubuntu_data'

    extracted_corpus_path = os.path.join(
        path,
        '**','**','**', '*.tsv'
    )


    def my_test(self):
        try:
            def chunks(items, items_per_chunk):
                for start_index in range(0, len(items), items_per_chunk):
                    end_index = start_index + items_per_chunk
                    yield items[start_index:end_index]

            tagger = PosLemmaTagger(languages.ENG)

            file_list = glob.glob(self.extracted_corpus_path)
            #
            file_groups = tuple(chunks(file_list, 10000))

            start_time = time.time()
            df = pd.DataFrame(columns=['date', 'from', 'to', 'content'])

            for tsv_files in file_groups:

                statements_from_file = []

                for tsv_file in tsv_files:
                    # df = df.append(pd.read_csv(tsv_file, delimiter='\t',header=None,names=['date','from','to','content']), ignore_index=True)

                    with open(tsv_file, 'r', encoding='utf-8') as tsv:
                        print("reading {}".format(tsv_file))
                        reader = csv.reader(tsv, delimiter='\t')

                        previous_statement_text = None
                        previous_statement_search_text = ''

                        for row in reader:
                            if len(row) > 0:
                                statement = Statement(
                                    text=row[3],
                                    in_response_to=previous_statement_text,
                                    conversation='training',
                                    created_at= parse(row[0]),
                                    persona=row[1]
                                )

                                # for preprocessor in ChatBot.preprocessors:
                                #     statement = preprocessor(statement)
                                # print("Statment content:\n{}".format(statement))
                                statement.search_text = tagger.get_bigram_pair_string(statement.text)
                                statement.search_in_response_to = previous_statement_search_text

                                previous_statement_text = statement.text
                                previous_statement_search_text = statement.search_text

                                statements_from_file.append(statement)
                print(statement)
                # self.chatbot.storage.create_many(statements_from_file)
            # df.to_csv(r'ubuntus_cs_log.csv',index=False, sep='\t')
        except:
            traceback.print_exc()


if __name__ == '__main__':
    myTrainer().my_test()