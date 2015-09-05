from textblob import TextBlob
import text_repository
def main():
    start_program_loop()
    map_texts_to_sentiments()
    return




def start_program_loop():
    sentiment_mapping = map_texts_to_sentiments()
    ngram_mapping = map_texts_to_ngrams()
    print(ngram_mapping)
    print(text_repository.raven_text.sentiment)
    print(text_repository.raven_text.ngrams(5))

    while True:
        sentiment = get_sentiment_from_ben()
        get_text_by_sentiment(sentiment)


def get_text_by_sentiment(sentiment):
    return


def map_texts_to_sentiments():
    return {x[0:5]: x.sentiment.polarity for x in text_repository.all_texts}


def map_texts_to_ngrams(default_ngram_size = 3):
    return {x[0:5]: make_dictionary_from_ngram(x.ngrams(default_ngram_size)) for x in text_repository.all_texts}


def make_dictionary_from_ngram(ngram_list):
    return {x[0]: ngram_list[1:] for x in ngram_list}


def get_sentiment_from_ben():
    return 10
    #cuz ben is on the struggle bus atm


if __name__ == "__main__":
    main()
