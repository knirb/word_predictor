import nltk
from nltk.util import ngrams
import codecs

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

    def guess_next_word_unigram(self):

        words_freq_dist = nltk.FreqDist(self.tokens)
        unigram_most_common = words_freq_dist.most_common(3)
        if(guess_1 == "i"):
            guess_1 = "I"
        if(guess_2 == "i"):
            guess_2 = "I"
        if(guess_3 == "i"):
            guess_3 = "I"
        guess_1, guess_2, guess_3 = self.parse_most_common_output(unigram_most_common)

        return guess_1, guess_2, guess_3

    def guess_next_word_bigram(self, prev_word):

        bigram_most_common = self.bigram_freq[prev_word.lower()].most_common(3)
        guess_1, guess_2, guess_3 = self.parse_most_common_output(bigram_most_common)

        return guess_1, guess_2, guess_3

    def guess_next_word_trigram(self, prev_prev_word, prev_word):

        trigram_most_common = self.trigram_freq[(prev_prev_word.lower(),prev_word.lower())].most_common(3)
        guess_1, guess_2, guess_3 = self.parse_most_common_output(trigram_most_common)

        return guess_1, guess_2, guess_3

    def finish_word(self, current_word):

        words_with_same_start = []

        for token in self.tokens:
            if token.startswith(current_word):
                words_with_same_start.append(token)

        finish_word_freq_dist = nltk.FreqDist(words_with_same_start)
        most_common_words = finish_word_freq_dist.most_common(3)

        guess_1, guess_2, guess_3 = self.parse_most_common_output(most_common_words)

        return guess_1, guess_2, guess_3

    def parse_most_common_output(self, most_common_words):
        if len(most_common_words) == 3:
                guess_1, guess_2, guess_3 = most_common_words
                guess_1, guess_2, guess_3 = guess_1[0], guess_2[0], guess_3[0]
        elif len(most_common_words) == 2:
            guess_1, guess_2 = most_common_words[0][0], most_common_words[1][0]
            guess_3 = None
        elif len(most_common_words) == 1:
            guess_1 = most_common_words[0][0]
            guess_2, guess_3 = None, None
        else:
            guess_1, guess_2, guess_3 = None, None, None
        return guess_1, guess_2, guess_3



# # do we want spell check
# min_1 = 1000
# min_2 = 1000
# min_3 = 1000
# guess_1 = ""
# guess_2 = ""
# guess_3 = ""

# for token in self.tokens:

    # edit_distance = nltk.edit_distance(token[:len(current_word)],current_word)
    # if token != guess_1 and token != guess_2 and token != guess_3:
    #     if edit_distance < min_1:
    #         min_1 = edit_distance
    #         guess_1 = token
    #     elif edit_distance < min_2 :
    #         min_2 = edit_distance
    #         guess_2 = token
    #     elif edit_distance < min_3 :
    #         min_3 = edit_distance
    #         guess_3 = token
