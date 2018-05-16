# normal version of word frequency program

import operator
my_dict = {}

with open('sample.txt') as infile:
    my_contents = infile.read()
    my_words = my_contents.lower().replace("!", "").replace(":", "").replace(".", "").replace("\n", " ").replace("?", "").replace("-", " ").replace(",", " ").split()

    for word in my_words:

        if word not in my_dict:
            my_dict[word] = 0
        my_dict[word] += 1



most = sorted([(key,value) for (value,key) in my_dict.items()], reverse=True)

shortened = dict((key,value) for (key, value) in most if key > 420)

for key, value in shortened.items():
    print (value, key)
