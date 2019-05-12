import nltk
from nltk.util import ngrams
import codecs
from collections import defaultdict


class WordPredictor(object):

    def process_file(self, f):
        with codecs.open('corpus.txt', 'r', 'utf-8') as text_file:
            text = str(text_file.read()).lower()
        try :
            self.tokens = nltk.word_tokenize(text)
        except LookupError:
            nltk.download('punkt')
            self.tokens = nltk.word_tokenize(text)
    
    def __init__(self):
        self.tokens = []
        self.bigram_model = []
        self.trigram_model = []
        self.bigram_freq = []
        self.trigram_freq = []

    def create_bigram(self):
        self.bigram_model = list(ngrams(self.tokens, 2))
        self.bigram_freq = nltk.ConditionalFreqDist(self.bigram_model)

    def create_trigram(self):
        self.trigram_model = list(ngrams(self.tokens, 3))
        trigrams_as_bigrams = []
        trigrams_as_bigrams.extend([((t[0],t[1]), t[2]) for t in self.trigram_model])
        self.trigram_freq = nltk.ConditionalFreqDist(trigrams_as_bigrams)

    def guess_next_word_bigram(self, prev_word):
        # bigram model
        try:
            bigram_most_common = self.bigram_freq[prev_word.lower()].most_common(3)
            guess_1 = bigram_most_common[0][0]
            guess_2 = bigram_most_common[1][0]
            guess_3 = bigram_most_common[2][0]
        except:
            guess_1 = None
            guess_2 = None
            guess_3 = None
        return guess_1, guess_2, guess_3

    def guess_next_word_trigram(self, prev_prev_word, prev_word):
        # trigram model
        try:
            trigram_most_common = self.trigram_freq[(prev_prev_word.lower(),prev_word.lower())].most_common(3)
            guess_1 = trigram_most_common[0][0]
            guess_2 = trigram_most_common[1][0]
            guess_3 = trigram_most_common[2][0]
        except:
            guess_1 = None
            guess_2 = None
            guess_3 = None
        return guess_1, guess_2, guess_3

def main():
    word_predictor = WordPredictor()
    word_predictor.process_file("corpus.txt")

    user_input = "This is a "
    user_word_list = user_input.split()

    guess_1 = ""
    guess_2 = ""
    guess_3 = ""

    if user_input[-1] == " " and len(user_word_list) == 1:
        word_predictor.create_bigram()
        guess_1, guess_2, guess_3 = word_predictor.guess_next_word_bigram(user_word_list[0])

    elif user_input[-1] == " " and len(user_word_list) >= 2:
        word_predictor.create_trigram()
        guess_1, guess_2, guess_3 = word_predictor.guess_next_word_trigram(user_word_list[-2], user_word_list[-1])

    print(guess_1, guess_2, guess_3)


if __name__ == "__main__":
    main()


    









