__author__ = 'piatskia'
from textblob import TextBlob
import random

def get_num_lines():
    return 5

class Corpus:
    def __init__(self, text):
        self.text_blob = TextBlob(text)
        self.n_gram = self.text_blob.ngrams(3)
        # key: sentiment, wordlist
        self.n_gram_dict = {x[0]: (TextBlob(x[0]).sentiment, x[1:]) for x in self.n_gram}
        self.sentiment = self.text_blob.sentiment

    def get_line(self, head_word):
        line = ""
        prev_word = self.get_next_word(head_word)
        for _ in range(get_num_lines()):
            line += " " + prev_word
            prev_word = self.get_next_word(prev_word)
        return line, prev_word

    # returns next word
    def get_next_word(self, keyword):

        # keep trying until we get a key with values
        while not keyword in self.n_gram_dict:
            # get random word
            keyword = random.choice(self.n_gram_dict.keys())

        wordlist = self.n_gram_dict[keyword][1]
        return random.choice(wordlist)


