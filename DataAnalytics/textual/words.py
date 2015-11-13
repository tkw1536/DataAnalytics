import re

from DataAnalytics.textual.stopwords import STOP_WORDS

VOWELS = ["a", "e", "i", "o", "u"]
VOWELSS = VOWELS + ["s"]
TERMINATORS = [",", ";", ".", ":", "?", "!", "-", "&", "(", ")"]

stem_word_cache = {}

def stem_word(word):
    """
        Turns a word into its stem word.

        word: Word to stem.
    """

    # if we have the stemmed word cached, return that
    if word in stem_word_cache:
        return stem_word_cache[word]
    original_word = word

    # strip off whitespaces
    word = word.lower().strip()

    # remove all the terminating characters
    for t in TERMINATORS:
        if word.endswith(t):
            word = word[:-len(t)]

    # check if the word ends with s and a non-s vowl
    if word.endswith("s") and len(word) > 1:
        if not word[-2] in VOWELSS:
            word = word[:-1]

    # if the word ends in es, drop the s
    if word.endswith("es"):
        word = word[:-1]

    # remove ing
    if word.endswith("ing"):
        _word = word[:-3]
        if _word != "th" and len(_word) > 1:
            word = _word

    # if a word ends with ed
    if word.endswith("ed"):
        if len(word) > 3:
            word = word[:-2]

    # ies
    if word.endswith("ies") and (not word.endswith("eies") or not word.endswith("aies")):
        word = word[:-3]+"y"

    # cache the word
    stem_word_cache[original_word] = word

    # and retun it
    return word

def find_words(text):
    """
        Finds all words in some text string.

        text: String to find all words in.
    """

    # words we want to find
    words = []

    # split all the worlds and map them
    text_words = re.split('\\s+', text)

    # stem all the words
    text_words = map(stem_word, text_words)

    # remove stop words
    text_words = filter(lambda x:not x in STOP_WORDS, text_words)

    return list(set(text_words))

def count_words(text, words):
    """
        Counts words in a string.

        text: Text to count words in.
        words: Words to count.
    """

    (nw, counts) = count_all_words(text, and_words = words)
    return counts[:len(words)]


def count_all_words(text, and_words = []):
    """
        Counts words in a string.

        text: Text to count words in.
        and_words: Additional words to count (that may or may not be in the data).
    """

    # initialise a list of words
    words = list(and_words)[:]

    # and a word count_vector
    word_counts = [0 for i in words]

    # split all the worlds and map them
    text_words = re.split('(\\s+|[\\+\\-\\(\\)\\[\\]\\{\\}])', text)

    # stem all the words
    text_words = map(stem_word, text_words)

    # remove stop words
    text_words = filter(lambda x:not x in STOP_WORDS, text_words)

    # go over each of the text words
    for t in text_words:

        # if it is already there, simply increase the count
        try:
            i = words.index(t)
            word_counts[i] += 1

        # if not append them
        except:
            words.append(t)
            word_counts.append(1)

    return (words, word_counts)
