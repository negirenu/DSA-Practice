# validate when we split a phrase , all the words exists in the list.
# input1, phrase 'themanran', word_list = ['the', 'itytg', 'ran', 'fer', 'man']
# output=['the', 'man', 'ran']
# input2, phrase 'themanran', word_list = ['itytg', 'ran', 'fer', 'man']
# output = []

def word_split(phrase, words, output=None):
    # base case
    if output is None:
        output = []

    for word in words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], words, output)
    return output


print(word_split('themanran', words=['itytg', 'ran', 'fer', 'man', 'the']))
