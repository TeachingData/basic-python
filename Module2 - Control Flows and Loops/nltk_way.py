from nltk import word_tokenize, ngrams, FreqDist
from nltk.corpus import stopwords
from urllib import request

## Create STOP word constant
STOP = stopwords.words('english')

### Get the file
resp = request.urlopen("http://www.gutenberg.org/files/12/12-0.txt")
raw = resp.read().decode('utf8')

""" 
tokenize all words, remove punctuation (or more ignore it), and give length
FYI - for most you have to actually strip all unicode punctuation which is 
another process but this file has spacing between the punctuation and words.
So just need to exclude non-alphanumeric chars.
"""
word_bag = [word.lower() for word in word_tokenize(raw) 
    if word not in STOP and word.isalnum()] 
print(len(word_bag))

## FreqDist is a frequency dict - or the nltk way to make a Counter
## So we just print everthing the same way
unigrams = FreqDist(word_bag)
total = sum(unigrams.values())
for word, freq in unigrams.most_common(5):
  print("The word '{}' appeared {} times or {:3f} percent".format(
    word, freq, freq/total * 100))

print("\n----------------------\n")

my_bigrams = FreqDist(ngrams(word_bag, 2))
for words, freq in my_bigrams.most_common(5):
  print("The word '{}' was before '{}' {} times".format(
    words[0], words[1], freq))
