from model import nlp_processor

# Tokenization Empty Behavior
def test_tokenization_empty():
    message = ""
    result = nlp_processor.tokenization(message)
    assert result == []

# Tokenization Single Spaces
def test_tokenization_single_spaces():
    message = "asd a aa s a"
    result = nlp_processor.tokenization(message)
    assert result == ["asd","a","aa","s","a"]

# Tokenization Multiple Spaces
def test_tokenization_multiple_spaces():
    message = "asd  \t  a  \v   \f aa   \r s  \n  a"
    result = nlp_processor.tokenization(message)
    assert result == ["asd","a","aa","s","a"]

# Tokenization Trailing Spaces
def test_tokenization_trailing_spaces():
    message = "  \t  \v   \f   \r     asd  a aasa    \n   "
    result = nlp_processor.tokenization(message)
    assert result == ["asd","a","aasa"]

# Tokenization Only Spaces
def test_tokenization_spaces_all():
    message = "  \t  \v   \f   \r       \n   "
    result = nlp_processor.tokenization(message)
    assert result == []

# Tokenization No Spaces
def test_tokenization_spaces_none():
    message = "sajdlkasjkldjaslkdjlkasjdlkasjdkla"
    result = nlp_processor.tokenization(message)
    assert result == ["sajdlkasjkldjaslkdjlkasjdlkasjdkla"]
