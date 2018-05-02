import re
from SyllableCounter import syllables
FileObject = open("TestDocument", "r")
file_contents = FileObject.read()

def counting():

    syllablecount = 0

    beg_each_Sentence = re.findall(r"\.\s*(\w+)", file_contents)
    capital_words = re.findall(r'\b[A-Z][a-z]+\b', file_contents)
    with open("TestDocument", "r") as f:
        words = f.read().split()
    for word in words:
        if word not in capital_words and len(word) >= 3: #all lower case words

            if syllables(word) >= 3:
                syllablecount += 1

        if word in capital_words and word in beg_each_Sentence: #beginning of each sentence is uppercase

            if syllables(word) >= 3:
                syllablecount += 1
    return syllablecount

def wordcount():
    # Regex to match all words, hyphenated words count as a compound words
    return len(re.findall("[a-zA-Z-]+", file_contents))

def sentencecount():
    #regex to count sentences, can end with a period, "?" or "!"
    return (len(re.split("[.!?]+", file_contents))-1)


FileObject.close()
