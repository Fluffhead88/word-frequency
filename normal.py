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



most = sorted([(k,v) for (v,k) in my_dict.items()], reverse=True)

sorted = dict((key,value) for key, value in most if key > 420)

print (sorted)
#def sort_words(x):
#    return x[1]
#sorted(my_dict, key=sort_words)
