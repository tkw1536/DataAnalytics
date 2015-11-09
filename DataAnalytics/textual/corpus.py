import numpy as np
from DataAnalytics.textual.words import find_words, count_all_words, stem_word

def to_matrix(documents, n = 0, words = None):
    """
        Turns an array of documents into a matrix of word frequencies

        documents: Array of strings to check.
        n: Will only take the n words that occur most frequently. If n=0, take all words.
        words: Optional. Words to count.
    """

    # if we have no words yet set them as basic words
    if words == None:
        words = []
    else:
        words = list(map(words, stem_word))

    # introduce an array of words
    counts = [[] for d in documents]

    for i, d in enumerate(documents):
        # count the number of words we had before
        wl = len(words)

        # count all the words and update the counts
        (words, counts[i]) = count_all_words(d, and_words = words)

        # generate an array of zeros to add to the previous numbers
        wl = [0]*(len(words) - wl)

        # and add them to the matrix
        for j in range(i):
            counts[j] += wl

    # turn it into a matrix now
    words_matrix = np.array(counts)

    # if given specifically take only the first n indexes
    if n > 0:
        # count all the word frequencies
        word_frequences = np.sum(words_matrix, axis=0)

        # find the top word indexes
        top_words_indexes = np.argsort(word_frequences)[::-1][:n]

        # update the words array
        words = [words[i] for i in list(top_words_indexes)]

        # update the words matrix
        words_matrix = words_matrix[:, top_words_indexes]


    # return found words and word matrix
    return words, words_matrix
