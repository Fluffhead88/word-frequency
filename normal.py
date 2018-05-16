# normal version of word frequency program

my_dict = {}

with open('sample.txt') as infile:
    my_contents = infile.read()
    for words in my_contents:
        my_words = my_contents.split().lower().replace("!", "").replace(":", "").replace(".", "").replace("/n", "").replace("#", "").replace("?", "").replace(("-", "").replace(",", "")





        for word in my_words:
            if word not in my_dict:
            my_dict[word] = 0
            my_dict[word] += 1
            if my_dict[word] > 40
            print my_dict[word]
