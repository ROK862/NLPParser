import nltk
import sys
import re

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP
S -> S PP
S -> S Conj S
S -> S P S
NP -> N 
NP -> Det NP
NP -> Det Adj NP
NP -> Det Adj 
NP -> Adj NP
NP -> NP PP 
NP -> NP Conj NP 
NP -> NP Adv
VP -> V 
VP -> VP NP 
VP -> VP PP 
VP -> VP Conj VP 
VP -> V Adv 
PP -> P NP 
PP -> NP P 
"""


grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """

    # Convert sentence to lowercase
    sentence = sentence.lower()

    # Tokenize sentence into words
    words = nltk.word_tokenize(sentence)

    # Remove any word that does not contain at least one alphabetic character
    words = [w for w in words if re.search('[a-zA-Z]', w)]

    return words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """

    np_chunks = []
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            if not any(child.label() == "NP" for child in subtree.subtrees() if child != subtree):
                np_chunks.append(subtree)
    return np_chunks


if __name__ == "__main__":
    main()
