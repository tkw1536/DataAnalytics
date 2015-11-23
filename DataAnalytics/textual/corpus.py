import numpy as np
from DataAnalytics.distances import order_by_distance
from DataAnalytics.textual.words import find_words, count_words, count_all_words, stem_word


def query_to_index(query, IDF, words, M, d=None):
    """
        Queries for similar document in a word count matrix.

        query: New document to search for.
        IDF: IDF vector
        words: Words the word count matrix consists of.
        M: Term Importance matrix.
        d: Distance Function ( = metric) to use.
    """

    # count words inside this vector
    vquery = IDF*count_words(query, words=words)

    # split all our documents
    docs = np.split(M, M.shape[0], axis=0)

    # and return the best documents by index
    return order_by_distance(vquery, docs, d)


def make_TIM(M):
    """
        Makes a term importance matrix from a word count matrix.

        M: Word count matrix to transform.
    """

    N = M.shape[0]

    # generate a matrix of zeros and ones
    ZO = np.zeros(M.shape)
    for x in range(M.shape[0]):
        for y in range(M.shape[1]):
            ZO[x][y] = 1 if M[x][y] > 0 else 0

    # compute the IDFs
    wj = np.sum(ZO, axis=0)
    wj = np.array([max(1, j) for j in wj])
    IDF = np.log(N / wj)

    # return a term importatnce matrix
    return (IDF, IDF*M)

def word_count_matrix(documents, n = 0, words = None, stop_words = None):
    """
        Turns an array of documents into a word count matrix.

        documents: Array of strings to check.
        n: Will only take the n words that occur most frequently. If n=0, take all words.
        words: Optional. Words to count.
        stop_words: Optional. Words to ignore.
    """

    # if we have no words yet set them as basic words
    if words == None:
        words = []
    else:
        words = list(map(stem_word, words))

    if stop_words == None:
        stop_words = []
    else:
        stop_words = list(map(stem_word, stop_words))

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

    # indexes to remove
    indexes_remove = list(map(lambda p:p[0], filter(lambda p:p[1] in stop_words,enumerate(words))))

    # remove stop words
    words_matrix = np.delete(words_matrix, indexes_remove, axis=0)
    words = np.delete(words, indexes_remove).tolist()

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
