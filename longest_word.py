# print the longest word in a sentence or a line of words

def longest_word(line):
    import numpy as np

    words = line.split()

    lengths=[""]*len(words)
    for i in range(0, len(words)):
        lengths[i]=len(words[i])

    index=lengths.index(np.max(lengths))
    return(words[index])

#test the function

line = "Print Print the longest word in the sentence"

longest_word(line)