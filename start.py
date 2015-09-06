from textblob import TextBlob
from os import listdir
from os import getcwd
from os.path import isfile, join
from corpus import Corpus
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def main():
    start_program_loop()
    #map_texts_to_sentiments()
    return

def start_program_loop():
    all_texts = []
    for dir_entry in listdir(getcwd()+ "/texts"):
        file = open(getcwd() + "/texts/" + dir_entry)
        all_texts.append(file.read())
    poem = ""
    x = 0
    corpi = initialize_all_corpi(all_texts)
    sentiment_mapping = map_corpi_to_sentiments(corpi)
    prev_word = ""
    current_line = ""
    while x < 10:
        raw_emotion_scalar = get_sentiment_from_ben()
        corpus = get_corpus_by_sentiment(raw_emotion_scalar, sentiment_mapping, corpi)

        current_line, prev_word = generate_line(corpus, prev_word)
        poem += current_line
        print(current_line)
        x += 1


def initialize_all_corpi(all_texts):
    return map(lambda x: Corpus(x), all_texts)


def get_corpus_by_sentiment(raw_emotion_scalar, sentiment_mapping, corpi):
    return corpi[2]


def map_corpi_to_sentiments(corpi):
    return {x: x.sentiment for x in corpi}


def map_texts_to_ngrams(default_ngram_size = 3):
    return {x[0:5]: make_dictionary_from_ngram(x.ngrams(default_ngram_size)) for x in text_repository.all_texts}


def make_dictionary_from_ngram(ngram_list):
    return {x[0]: ngram_list[1:] for x in ngram_list}


def get_sentiment_from_ben():
    return 10

def generate_line(corpus, prev_word):
    return corpus.get_line(prev_word)

if __name__ == "__main__":
    main()
