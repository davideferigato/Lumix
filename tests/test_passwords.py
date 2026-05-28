from lumix.passwords.generate import generate_password


def test_generate_password():
    pwd = generate_password(10)
    assert len(pwd) == 10
    pwd_sym = generate_password(12, use_symbols=True)
    assert len(pwd_sym) == 12

