import os
from re import sub
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

## Add word to set if it meets our conditions (map - reduce so this is the map)
## so after this we would have "basketball, 1"
def word_mapper(article):
    for word in word_tokenize(article):
        ## remove 's & special characters besides - (hyphen)
        word = sub("'s|[^A-Za-z0-9\-]+", "", word.lower())
        if len(word) > 2 and word not in stopwords.words('english'):
            yield(word, 1)

## now we feed the mapper into the reducer and sum up all those 1s
### so (ball, 1), (ball, 1), (ball, 1) would return (ball, 3)
def word_reducer(word, counts):
    yield (word, sum(counts))

## final function which just puts the map with the reduce
#### note we are combining everything this time because that's better
#### for predictive modeling (rather than categorization training)
def mapreducer(files):
    collector = defaultdict(list) #to hold all the counts
    ### fyi - cannot use a Counter for this because its a Class object
       #### we would need to do value += 1 again not sum all values at once
    ### whereas defaultdict is an extension of dictionary

    for current_file in files:
        with open(current_file) as f:
            for token, count in word_mapper(f.read()):
                collector[token].append(count)

    return [the_count
            for token, counts in collector.items()
            for the_count in word_reducer(token, counts)]


with os.scandir("articles") as files:
    print(sorted(mapreducer(files), key = lambda e: e[1], reverse = True))

        

        