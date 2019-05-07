import nltk
from nltk.util import ngrams
import codecs

with codecs.open("corpus.txt", 'r', 'utf-8') as text_file:
  text = str(text_file.read()).lower()
tokens = nltk.word_tokenize(text)
output = list(ngrams(tokens, 5))
print(output)






