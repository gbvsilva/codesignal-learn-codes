import re
from collections import defaultdict

def rare_words_finder(text):
    # implement this
    counter = defaultdict(int)
    for word in text.split():
        counter[word.lower()] += 1
    return list(counter.items())

print(rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks")) # Expected Output: [('hey', 1), ('there', 1), ('hot', 1), ('shot', 1), ('are', 1)]

print(rare_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy")) # Expected Output: [('brown', 1), ('jumps', 1), ('over', 1), ('but', 1), ('quick', 2)]

print(rare_words_finder("")) # Expected Output: []
