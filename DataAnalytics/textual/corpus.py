import numpy as np
from DataAnalytics.textual.words import find_words, count_words, stem_word

def to_matrix(documents, n = 0, words = None):
    """
        Turns an array of documents into a matrix of word frequencies

        documents: Array of strings to check.
        n: Will only take the n words that occur most frequently. If n=0, take all words.
        words: Optional. Words to count.
    """

    if words != None:
        all_words = list(set(map(stem_word, words)))
    else:
        # create an array with all words
        all_words = set()

        # find all the words
        for d in documents:
            all_words.update(find_words(d))

        # make it a list
        all_words = list(all_words)

    # create a words matrix
    words_matrix = np.zeros((len(documents), len(all_words)))

    # count all the words
    for (i, d) in enumerate(documents):
        words_matrix[i] = count_words(d, all_words)

    # if given specifically take only the first n indexes
    if n > 0:
        # count all the word frequencies
        word_frequences = np.sum(words_matrix, axis=0)

        # find the top word indexes
        top_words_indexes = np.argsort(word_frequences)[::-1][:n]

        # update the words array
        all_words = [all_words[i] for i in list(top_words_indexes)]

        # update the words matrix
        words_matrix = words_matrix[:, top_words_indexes]


    # return found words and word matrix
    return all_words, words_matrix
