# normal version of word frequency program

with open('sample.txt') as infile:
    my_contents = infile.read()
    my_contents.replace("!", "").replace(",", "").replace(":", "").replace(".", "").replace("/n", "").replace("*", "").replace("#", "").replace("?", "")
    my_contents.lower()
    my_content.replace("(", "").replace(")", "")
    my_contents.replace(("-", "").replace("[", "").replace("]", "").replace(""", "")
    
