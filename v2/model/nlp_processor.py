# Natural Language Processing helpers #

import string

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
    tokens = message.split()

    return tokens

def stop_word_removal(tokens, stop_word_list):

    # Preprocessed Text
    cleanedText = []

    # Loop through all token and remove the stop words
    for token in tokens:
        if token not in stop_word_list:
            cleanedText.append(token)

    return cleanedText
    