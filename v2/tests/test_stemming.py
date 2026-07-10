from model import nlp_processor

# Stemming empty behavior
def test_stemming_empty():
    word_list = []
    result = nlp_processor.stemming(word_list)
    assert result == []

# Stemming spaces
def test_clean_stop_words_empty_words():
    word_list = [" ","\t"," \n"," \v"," \r"," \f"]
    result = nlp_processor.stemming(word_list)
    assert result == [" ","\t"," \n"," \v"," \r"," \f"]

# Stemming a normal sentence
def test_stemming_sentence():
    word_list = ["i","started","running","recently","i","was","walking","my","neighbours","dog","and","loved","the","physical","activity"]
    result = nlp_processor.stemming(word_list)
    assert result == ["i", "start", "run", "recent", "i", "wa", "walk", "my", "neighbour", "dog", "and", "love", "the", "physic", "activ"]

# Stemming a sentence with spaces
def test_stemming_sentence_spaces():
    word_list = ["i"," ","started"," ","running"," ","recently"," ","i"," ","was"," ","walking"," ","my"," ","neighbours"," ","dog"," ","and"," ","loved"," ","the"," ","physical"," ","activity"]
    result = nlp_processor.stemming(word_list)
    assert result == ["i", " ", "start", " ", "run", " ", "recent", " ", "i", " ", "wa", " ", "walk", " ", "my", " ", "neighbour", " ", "dog", " ", "and", " ", "love", " ", "the", " ", "physic", " ", "activ"]

# Stemming suffix words
def test_stemming_suffix_words():
    word_list = ["running","jumped","studies","playing","happily","connected","fishing","organized","walking","dogs"]
    result = nlp_processor.stemming(word_list)
    assert result == ["run","jump","studi","play","happili","connect","fish","organ","walk","dog"]

# Stemming normal suffix words
def test_stemming_suffix_normal_words():
    word_list = ["cat", "dog", "run", "walk", "eat", "fox", "bird", "chair", "milk", "bread"]
    result = nlp_processor.stemming(word_list)
    assert result == ["cat", "dog", "run", "walk", "eat", "fox", "bird", "chair", "milk", "bread"]