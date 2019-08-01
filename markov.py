"""Generate Markov text from text files."""

from random import choice
import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open("green-eggs.txt").read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()


    i = 0

    while i < len(words)-2:
        new_tuple = (words[i], words[i+1])
        if new_tuple not in chains.keys():
            chains[new_tuple] = [words[i+2]]
        elif new_tuple in chains.keys():
            chains[new_tuple].append(words[i+2])
        i +=1


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # random_phrase = random.choice(chains.keys())
    random_phrase = ('Would', 'you')
    words.append(random_phrase[0])
    words.append(random_phrase[1])

    while random_phrase != ('Sam', 'I'):
        random_phrase = (random_phrase[1], random.choice(chains[random_phrase]))
        words.append(random_phrase[1])

    words.append('am?')


    return " ".join(words)
    # return words



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
