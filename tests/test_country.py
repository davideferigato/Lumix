from lumix.country.convert import code_to_name, name_to_code


def test_code_to_name():
    assert code_to_name("IT", "en") == "Italy"
    assert code_to_name("IT", "it") == "Italia"

def test_name_to_code():
    assert name_to_code("Italy", "en") == "IT"
    assert name_to_code("Italia", "it") == "IT"

