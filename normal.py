# normal version of word frequency program

my_dict = {}

with open('sample.txt') as infile:
    my_contents = infile.read()
    my_words = my_contents.lower().replace("!", "").replace(":", "").replace(".", "").replace("\n", "").replace("#", "").replace("?", "").replace("-", "").replace(",", "").split()

    for word in my_words:

        if word not in my_dict:
            my_dict[word] = 0
        my_dict[word] += 1
        if my_dict[word] > 2800:
            print (my_dict[word])
