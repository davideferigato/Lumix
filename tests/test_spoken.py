from lumix.spoken.convert import number_to_words


def test_number_to_words_en():
    assert number_to_words(123, "en") == "one hundred twenty-three"
    assert number_to_words(1000, "en") == "one thousand"


def test_number_to_words_it():
    assert number_to_words(123, "it") == "cento ventitre"
    assert number_to_words(1000, "it") == "mille"
