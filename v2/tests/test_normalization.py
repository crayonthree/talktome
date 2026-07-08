from model import nlp_processor

# Normalization Empty Behavior
def test_normalization_empty():
    message = ""
    result = nlp_processor.normalize_text(message)
    assert result == ""

# Normalization lowercase conversion test
def test_normalization_lowercase():
    message = "ABSCabscLkL"
    result = nlp_processor.normalize_text(message)
    assert result == "abscabsclkl"

def test_normalization_lowercase_all():
    message = "ABSCABSCLKL"
    result = nlp_processor.normalize_text(message)
    assert result == "abscabsclkl"

def test_normalization_lowercase_none():
    message = "abscabsclkl"
    result = nlp_processor.normalize_text(message)
    assert result == "abscabsclkl"

# Normalization punctuation removal test
def test_normalization_punctuation():
    message = "asbdnmsda!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~sadasdas"
    result = nlp_processor.normalize_text(message)
    assert result == "asbdnmsda                                sadasdas"

def test_normalization_punctuation_all():
    message = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    result = nlp_processor.normalize_text(message)
    assert result == ""

def test_normalization_punctuation_none():
    message = "asbdnmsdasadasdas"
    result = nlp_processor.normalize_text(message)
    assert result == "asbdnmsdasadasdas"

# Normalization trailing whitespace test
def test_normalization_trailing_space_test():
    message = "   asbdnmsda      asdsa "
    result = nlp_processor.normalize_text(message)
    assert result == "asbdnmsda      asdsa"

def test_normalization_trailing_space_test_all():
    message = "                                                                     "
    result = nlp_processor.normalize_text(message)
    assert result == ""

def test_normalization_trailing_space_test_none():
    message = "asb  dn  msda      sada   sda s"
    result = nlp_processor.normalize_text(message)
    assert result == "asb  dn  msda      sada   sda s"

# Normalization combination
def test_normalization_combination_one():
    message = "jadklaskljdlkasAKSDJLJSDKLJADKSA@!#@!#!@*#()!@*#()!@#: LDK:LDA:DLKLSKD:S da dsad asd SDSD Das das ldasd ADS S D ASDA#@!#!"
    result = nlp_processor.normalize_text(message)
    assert result == "jadklaskljdlkasaksdjljsdkljadksa                       ldk lda dlklskd s da dsad asd sdsd das das ldasd ads s d asda"