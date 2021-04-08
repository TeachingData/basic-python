import os
from collections import Counter
## Love counter: built-in dictionary for..... counting

## Now a simple way to check for items is to run a decision tree using if/else if/else branching and branching
## if (word == "basketball" & confidence > 1.5) {...}
###.....or we can build the try with a dictionary & Counter 
# counter keeps insert order which is helpful :)
### Do not use this method - better to make a class or move to numpy but its a good explaination

STOP = {'the', 'and', "from", "who", "there", "one's", 
        "has", "their", "own", "which", "each", "for", "are"}

with os.scandir("articles") as files:
    for current_file in files:

        word_bag = Counter()
        total = 0

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
            for token in f.read().split(): # cause token = word
                if len(token) > 2 and token.lower() not in STOP:
                    word_bag[token.lower()] += 1
                    total += 1

        print("-------------------------------------------------------")
        print(f"Starting book {current_file.name}")
        print(f"Total significant words (total - stop words) = {total}")
        
        for word, freq in word_bag.items():
            percent = (freq/total) * 100

            for cat in catagory_strength:
                if word in catagory_strength[cat]["features"]:
                    ## start by just counting whole
                    ##catagory_strength[cat]["count"] += 1
                    ## Then change to the percent as a weight
                    catagory_strength[cat]["count"] += percent

        topcat = {"cat": "Unknown", "value": 0.0}
        ## cause if nothing has 1 then its Unknown
        for cat in catagory_strength:
            if catagory_strength[cat]["count"] > topcat["value"]:
                topcat["cat"] = cat
                topcat["value"] = catagory_strength[cat]["count"]

        ## next line for testing
        #print(catagory_strength)
        print("The book is about {} with a score of {:.2f}".format(
            topcat["cat"], topcat["value"]
        ))