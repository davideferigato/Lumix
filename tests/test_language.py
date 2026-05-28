from lumix.language.convert import code_to_name, name_to_code


def test_code_to_name():
    assert code_to_name("en", "en") == "English"
    assert code_to_name("en", "it") == "Inglese"


def test_name_to_code():
    assert name_to_code("Italian", "en") == "it"
    assert name_to_code("Italiano", "it") == "it"
