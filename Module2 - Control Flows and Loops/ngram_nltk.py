import os
from re import sub
from nltk import word_tokenize, ngrams, FreqDist
from nltk.corpus import stopwords

## Create STOP word constant
STOP = stopwords.words('english')

with os.scandir("articles") as files:
    for current_file in files:
        ## The catagories and strengths we will compare
        # first time use ints (0)
        catagory_strength = {
           "Outdoor Hobbies": {
                "features": ("hiking", "rock", "climbing", "biking", "river", "lake",
                            "camping", "skiing", "outdoors", "glamping", "horse", 
                            "bird", "nature", "watching", "park", "paintball", 
                            "running", "swimming", "flowers", "gardening",
                            "campsite", "fishing", "campfire"),
                "count": 0.0
            },
            "Sports": {
                "features": ("football", "basketball", "ball", "sport", "sports", 
                        "players", "hockey", "team", "baseball", "soccer",
                        "bowling", "cycling", "golfing", "swimming"),
            "count": 0.0
            },
            "Travel": {
                "features": ("cruise", "exotic", "lands", "travel", "airplane", 
                    "boats", "boat", "road", "trip", "trips", "visit", 
                    "visited", "adventure", "adventured"),
            "count": 0.0
            },
            "Arts": {
                "features": ("drawing", "painting", "arts", "art", "photography", 
                    "dancing", "coloring", "draw", "color", "paint",
                    "filming", "sculpture"),
                "count": 0.0
            },
            "Music": {
                "features": ("music", "band", "instrument", "musical", "concert", 
                        "rock", "metal", "hiphop", "country", "dancing"),
                "count": 0.0
            },
            "Crafting": {
                "features": ("candle", "making", "arranging", "crafting", "craft", 
                        "diy", "knitting", "scrapbook", "scrapbooking"),
                "count": 0.0
            },
            "Food or Cooking": {
                "features": ("baking", "brewing", "canning", "cooking", "chef", 
                        "food", "wine", "tasting", "roasting", "groceries",
                        "grocery", "ingredients", "pancakes", "blueberries",
                        "raspberries", "chicken", "beef", "oatmeal", "rice"),
                "count": 0.0
            },
            "Games": {
                "features": ("board", "card", "video", "games", "game", "gaming", 
                        "puzzles", "poker", "trivia", "tabletop"),
                "count": 0.0
            }
        }

        with open(current_file) as f:
            word_bag = [sub("'s|[^A-Za-z0-9\-]+", "", token.lower()) for token in word_tokenize(f.read()) 
                if len(token) > 2 and token not in STOP] 

            print(word_bag)

            ## FreqDist is a frequency dict - or the nltk way to make a Counter
            ## So we just print everthing the same way
            unigrams = FreqDist(word_bag)
            total = sum(unigrams.values())
            for word, freq in unigrams.most_common(5):
                print("The word '{}' appeared {} times or {:3f} percent".format(
                    word, freq, freq/total * 100))

                print("\n----------------------\n")

            ##...fun part is bigrams and even tri (or any N) grams are easy too:
            my_bigrams = FreqDist(ngrams(word_bag, 2)) ## using same word_bag
            for words, freq in my_bigrams.most_common(5):
                print("The word '{}' was before '{}' {} times".format(
                    words[0], words[1], freq))

        

        