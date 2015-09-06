from os import listdir
from os import getcwd
from os.path import isfile, join
import random, sys

from textblob import TextBlob

from word import Word


last_word = ""

def main():
    parse_texts()
    loop()
    return

def loop():
    for _ in range(10): # while True
        sentiment_val = get_sentiment_value()
        get_next_line(sentiment_val)
    return

def get_next_line(sentiment_val):
    global last_word
    if not last_word:
        last_word = ""

    current_line, last_word = generate_line(sentiment_val, last_word)

    if is_noun(last_word):
        current_line += "\n"

    print current_line
    return current_line


### Parsing Functions
def parse_texts():
    texts_dir = getcwd() + "/texts"
    for dir_entry in listdir(texts_dir):
        text = open(texts_dir + "/" + dir_entry)
        contents = text.read()
        contents = contents.lower()
        text_to_ngrams(contents)
        text.close()
    return

def text_to_ngrams(text):
    blob = TextBlob(text)
    ngrams = blob.ngrams(NGRAM_SIZE)
    parse_ngrams(ngrams)
    return

def parse_ngrams(ngrams):
    for ngram in ngrams:
        word = ngram[0]
        phrase = " ".join(ngram[1:])
        phrase_sentiment = TextBlob(phrase).sentiment.polarity

        if word in all_words_dict:
            # word is in dictionary, add phrase to word.sentiment_ngrams_dict
            all_words_dict[word].sentiment_ngrams_dict[phrase_sentiment] = phrase
        else:
            # create new word and add to all_words_dict
            new_word = Word(word, {phrase_sentiment: phrase})
            all_words_dict[word] = new_word
    return

def is_noun(word):
    return TextBlob(word).tags[0][1] == 'NN'


### Generating poetry
# Returns the next line of poetry
def generate_line(sentiment, start_word):
    line, last_word = "", start_word
    next_phrase = get_next_phrase(sentiment, start_word)
    for _ in range(rand_num_lines()):
        line += " " + next_phrase
        last_word = next_phrase.split()[-1]
        next_phrase = get_next_phrase(sentiment, last_word)
    return str(line), last_word

def get_next_phrase(sentiment, word):

    # error checking - keep trying until we get a key with values
    while word not in all_words_dict:
        # get random word
        word = random.choice(all_words_dict.keys())

    phrase = get_closest_sentiment_phrase(sentiment, word)
    return phrase

def get_closest_sentiment_phrase(sentiment_val, word):
    # each key is a sentiment value between -1.0 and 1.0
    keys = all_words_dict[word].sentiment_ngrams_dict.keys()
    closest_key = min(keys, key=lambda x:abs(x-sentiment_val))
    phrase = all_words_dict[word].sentiment_ngrams_dict[closest_key]
    return phrase

def get_sentiment_value():
    return 1.0 # TODO - hook up with ben's side


### Helpers, Configuration, Random
def rand_num_lines():
    return random.randint(1, 3)


###
reload(sys)
sys.setdefaultencoding('utf8')
NGRAM_SIZE = 4

all_words_dict = {} # dictionary maps word to Word
parse_texts()


### Main
if __name__ == "__main__":
    main()


