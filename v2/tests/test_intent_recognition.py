from model import nlp_processor
from data import intents

# Intent word behavior
def test_intent_words():
    words_and_intents = {
    "hi": "Salutation",
    "bye": "Farewell",
    "thanks": "Thankful",
    "mood": "Mood",
    "time": "Time",
    "what": "Question" }

    for word, expected_intent in words_and_intents.items():
        words = []
        words.append(word)
        result = nlp_processor.intent_recognition(words,intents.intents)
        assert result == expected_intent

# Empty list behavior
def test_intent_empty():
    words = []
    result = nlp_processor.intent_recognition(words,intents.intents)
    assert result == "Unclear"

# Unknown Intent test
def test_intent_unknown():
    unclear_words = ["a","b","c","d","happens","you","really"]
    for word in unclear_words:
        words = []
        words.append(word)
        result = nlp_processor.intent_recognition(words,intents.intents)
        assert result == "Unclear"

# Space Intent test
def test_intent_spaces():
    unclear_words = [" ","\t","\r","\f","\n"]
    for word in unclear_words:
        words = []
        words.append(word)
        result = nlp_processor.intent_recognition(words,intents.intents)
        assert result == "Unclear"

# Intent count test
def test_intent_count():
    words = ["bye","bye","bye","hi","hi"]
    result = nlp_processor.intent_recognition(words,intents.intents)
    assert result == "Farewell"

# Intent prioritization test
def test_intent_prioritization_single():
    words = ["time","time","time","hi","hi","hi"]
    result = nlp_processor.intent_recognition(words,intents.intents)
    assert result == "Salutation"

# Intent prioritization test multiple intents
def test_intent_prioritization_multiple():
    words = ["time","time","time","hi","hi","hi","bye","bye"]
    result = nlp_processor.intent_recognition(words,intents.intents)
    assert result == "Salutation"