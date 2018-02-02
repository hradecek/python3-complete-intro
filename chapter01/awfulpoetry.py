#!/usr/bin/env python3

import random

articles = ["The", "A"]
subjects = ["cat", "dog", "man", "woman", "car", "movie", "neck", "body"]
verbs = ["danced", "sang", "jumped", "ran", "loved"]
adverbs = ["loudly", "quietly", "horribly"]

for _ in range(0, 5):
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    sentence = "{article} {subject} {verb}".format(
            article = article, subject = subject, verb = verb)
    if random.randint(0, 1) == 0:
        sentence += " {adverb}".format(adverb = random.choice(adverbs))
    print(sentence)
