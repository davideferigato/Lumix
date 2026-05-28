from lumix.phonetic.convert import text_to_phonetic


def test_text_to_phonetic():
    assert text_to_phonetic("CIAO") == "Charlie India Alpha Oscar"
    assert text_to_phonetic("HELLO") == "Hotel Echo Lima Lima Oscar"

