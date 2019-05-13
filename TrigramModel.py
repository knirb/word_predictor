import nltk
from nltk.util import ngrams
import codecs
from collections import defaultdict


class TrigramModel(object):
  """

  """
  def process_files(self, f):
    with codecs.open(f, 'r', 'utf-8') as text_file:
      text = str(text_file.read()).lower()
      try :
            self.tokens = nltk.word_tokenize(text)
            # self.unigram_count = dict(nltk.FreqDist(self.tokens))
            # self.total_words = len(self.tokens)
      except LookupError :
          nltk.download('punkt')
          self.tokens = nltk.word_tokenize(text)
      trigram = list(ngrams(self.tokens, 3))
      for triple in trigram:
        self.process_token(triple)

  def __init__(self):
        self.unigram_count = defaultdict(int)

        self.bigram_count = defaultdict(lambda: defaultdict(int))

        self.trigram_count = defaultdict(lambda: defaultdict(lambda:defaultdict(int)))

        self.unique_words = 0

        self.total_words = 0

  def process_token(self, triple):
    self.total_words += 1

    if triple[0] not in self.unigram_count:
        self.unique_words +=1
        self.unigram_count[triple[0]] = 1
    else:
        count = self.unigram_count[triple[0]]
        self.unigram_count[triple[0]] = count + 1

    self.bigram_count[triple[0]][triple[1]] += 1
    self.trigram_count[triple[0]][triple[1]][triple[2]] += 1


def main():
  trigram_model = TrigramModel()
  trigram_model.process_files("corpus.txt")
  print(trigram_model.trigram_count)
  #print(trigram_model.trigram_count["well"][","]["everyone"])

if __name__ == "__main__":
    main()
