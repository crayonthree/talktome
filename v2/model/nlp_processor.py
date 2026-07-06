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


# Intent Recognition
def intent_recognition(words, intents):

    # Dictionary to store intent counts
    intent = {}

    # Loop through all the stemmed words
    for word in words:
            
            for intent_term in intents.keys():
                if word in intents.get(intent_term).get("keywords"):
                    if intent_term not in intent:
                        intent[intent_term] = 1
                    else:
                        intent[intent_term] = intent[intent_term] + 1

    # Edge case if intent not found
    if not intent:
        return "Unclear"

    # Finding the max occurring intents and creating a dictionary for prioritization
    max_value = max(intent.values())
    core_intents = {key:val for key, val in intent.items() if val == max_value}

    # Check for prioritization
    if len(list(core_intents.keys())) >1:
        
        # Adding priority to intents to balance intents
        for intent_term in intents.keys():
            if intent_term in core_intents:
                core_intents[intent_term] = core_intents[intent_term] + intents.get(intent_term).get("priority")

    # Returning the intent based on occurences and/or priority
    return max(core_intents, key=core_intents.get)


# Function for processing flow
def nlp_processor(sentence, STOP_WORDS, intents):
    normalized_sentence = normalize_text(sentence)
    tokenized_sentence = tokenization(normalized_sentence)
    stop_word_removed_sentence = stop_word_removal(tokenized_sentence, STOP_WORDS)
    stemmedWords = stemming(stop_word_removed_sentence)
    intent = intent_recognition(stemmedWords, intents)

    return intent