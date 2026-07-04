# Natural Language Processing helpers #

import string
import nltk
from nltk.stem import PorterStemmer


# Normalizing text
def normalize_text(message):

    # Lowercase
    message = message.lower()

    # Create a mapping table and remove punctuation
    table = str.maketrans(string.punctuation, len(string.punctuation)*' ')
    message = message.translate(table)

    # Strip trailing whitespaces
    message = message.strip()
    
    return message


# Tokenization
def tokenization(message):

    # Tokenize on whitespaces
    words = message.split()

    return words


# Removing common insignificant words
def stop_word_removal(words, stop_word_list):

    # Preprocessed Text
    cleaned_words = []

    # Loop through all token and remove the stop words
    for word in words:
        if word not in stop_word_list:
            cleaned_words.append(word)

    return cleaned_words


# Stemming (removing word extensions)
def stemming(words):

    # Create a Porter Stemmer instance
    porter_stemmer = PorterStemmer()

    #Stemmed words after looping through all words and stemming
    root_words = [porter_stemmer.stem(word) for word in words]
    
    return root_words