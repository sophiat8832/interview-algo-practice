from Codewars.Weird_Strings.to_weird_case import to_weird_case

def test_single_word_small_word():
    assert to_weird_case("Is") == "Is"

def test_multiple_words():
    assert to_weird_case("This is a test") == "ThIs Is A TeSt"