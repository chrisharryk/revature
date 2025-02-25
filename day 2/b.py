# return the count of the words in a given sentence

def prog(sentence):
    return len(sentence.strip().split(' '))

print(prog('hi there, my name is harry'))