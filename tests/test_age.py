from lumix.age.convert import calculate_age


def test_calculate_age():
    age = calculate_age("1990-05-23")
    assert isinstance(age, int)
    assert age >= 0
