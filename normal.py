# normal version of word frequency program

with open('sample.txt') as infile:
    my_contents = infile.read()
    my_contents.replace("!", "").replace(":", "").replace(".", "").replace("/n", "").replace("*", "").replace("#", "").replace("?", "").replace(("-", "").replace(",", "")
    my_contents.lower()

    my_words = my_contents.split()

        my_dict = {}

    for word in my_words:
        if word not in my_dict.keys():
            my_dict[word] = 0
            my_dict[word] += 1
        if my_dict[word] > 40
        print my_dict[word]
