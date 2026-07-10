from model import nlp_processor
from data import stop_words

# Stop Word filter test
def test_clean_stop_words():
    word_list = ["the","blue","fox","obviously","loved","the","really","nice","people","of","townville","and","would","visit","them","very","regularly"]
    result = nlp_processor.stop_word_removal(word_list,stop_words.STOP_WORDS)
    assert result == ["blue","fox","loved","nice","people","townville","would","visit","them","regularly"]

# Stop word filter test only stop words
def test_clean_stop_words_all():
    word_list = ["on","at","for","and","or","but","very","obviously","lot","quite","really"]
    result = nlp_processor.stop_word_removal(word_list,stop_words.STOP_WORDS)
    assert result == []

# Stop word filter test no stop words
def test_clean_stop_words_none():
    word_list = ["blue","fox","loved","nice","people","townville","would","visit","them","regularly"]
    result = nlp_processor.stop_word_removal(word_list,stop_words.STOP_WORDS)
    assert result == ["blue","fox","loved","nice","people","townville","would","visit","them","regularly"]

# Stop word filter test empty strings
def test_clean_stop_words_empty_words():
    word_list = [" ","\t"," \n"," \v"," \r"," \f"]
    result = nlp_processor.stop_word_removal(word_list,stop_words.STOP_WORDS)
    assert result == [" ","\t"," \n"," \v"," \r"," \f"]

# Stop word filter test empty list
def test_clean_stop_words_empty_list():
    word_list = []
    result = nlp_processor.stop_word_removal(word_list,stop_words.STOP_WORDS)
    assert result == []

# Stop word filter test with combination of normal words, stop words, and spaces.
def test_clean_stop_words_combination():
    word_list = ["the","blue"," ","fox","obviously","loved","\t","the","really","nice","people","of","townville","and","\f","would","visit","them","very","regularly"]
    result = nlp_processor.stop_word_removal(word_list,stop_words.STOP_WORDS)
    assert result == ["blue"," ","fox","loved","\t","nice","people","townville","\f","would","visit","them","regularly"]