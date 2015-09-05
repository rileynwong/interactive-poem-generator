__author__ = 'piatskia'
from textblob import TextBlob

def get_num_lines():
    return 5

class Corpus:
    def __init__(self, text):
        self.text_blob = TextBlob(text)
        self.n_gram = self.text_blob.ngrams(3)
        self.n_gram_dict = {x[0]: x[1:] for x in self.n_gram}
        self.sentiment = self.text_blob.sentiment

    def get_line(self, head_word):
        line = ""
        prev_word = self.get_next_word(head_word)
        for _ in range(get_num_lines()):
            line += " " + prev_word
            prev_word = self.get_next_word(prev_word)
        return line, prev_word

    # returns next word
    def get_next_word(self, prev_word):
        if prev_word == "":
            prev_word = self.n_gram[0][0]
        return self.n_gram_dict[prev_word][0]
