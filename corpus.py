__author__ = 'piatskia'
from textblob import TextBlob

class Corpus:
    def __init__(self, text):
        self.text_blob = TextBlob(text)
        self.n_gram = self.text_blob.ngrams(3)
        self.n_gram_dict = {x[0]: x[1:] for x in self.n_gram}
        self.sentiment = self.text_blob.sentiment

    def get_line(self, head_word):
        # print(self.n_gram_dict);
        if head_word == "":
            head_word = self.n_gram[0][0]
        return " ".join(self.n_gram_dict[head_word])
