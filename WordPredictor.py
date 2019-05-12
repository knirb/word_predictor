import nltk
from nltk.util import ngrams
import codecs
from collections import defaultdict


class WordPredictor(object):

    def process_file(self, f):
        with codecs.open('corpus.txt', 'r', 'utf-8') as text_file:
            text = str(text_file.read()).lower()
        try :
            tokens = nltk.word_tokenize(text)
        except LookupError:
            nltk.download('punkt')
            tokens = nltk.word_tokenize(text)
    
    def parse_user_input(self, user_input):
        self.user_input = user_input
        self.user_word_list = user_input.split()
    
    def __init__(self):
        self.tokens = []
        self.bigram_model = []
        self.trigram_model = []
        self.bigram_freq = 0
        self.trigram_freq = 0
        self.user_input = ""
        self.user_word_list = []

    def create_bigram(self):
        self.bigram_model = list(ngrams(self.tokens, 2))
        self.bigram_freq = nltk.ConditionalFreqDist(self.bigram_model)

    def create_trigram(self):
        self.trigram_model = list(ngrams(self.tokens, 3))
        trigrams_as_bigrams = []
        trigrams_as_bigrams.extend([((t[0],t[1]), t[2]) for t in self.trigram_model])
        self.trigram_freq = nltk.ConditionalFreqDist(trigrams_as_bigrams)

    def guess_next_word(self):
        # bigram model
        if self.user_input[-1] == " " and len(self.user_word_list) == 1:
            print("bigram guess: ")
            try:
                bigram_most_common = bigram_freq[self.user_word_list[0].lower()].most_common(3)
                guess_1 = bigram_most_common[0][0]
                guess_2 = bigram_most_common[1][0]
                guess_3 = bigram_most_common[2][0]
            except:
                guess_1 = None
                guess_2 = None
                guess_3 = None
            print(guess_1, guess_2, guess_3)

        # trigram model
        if self.user_input[-1] == " " and len(self.user_word_list) >= 2:
            print("trigram guess:")
            try:
                trigram_most_common = trigram_freq[(self.user_word_list[-2].lower(), self.user_word_list[-1].lower())].most_common(3)
                guess_1 = trigram_most_common[0][0]
                guess_2 = trigram_most_common[1][0]
                guess_3 = trigram_most_common[2][0]
            except:
                guess_1 = None
                guess_2 = None
                guess_3 = None
            print(guess_1, guess_2, guess_3)

def main():
    word_predictor = WordPredictor()
    word_predictor.process_file("corpus.txt")

if __name__ == "__main__":
    main()


    









