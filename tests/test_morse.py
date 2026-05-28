from lumix.morse.convert import morse_to_text, text_to_morse


def test_text_to_morse():
    assert text_to_morse("SOS") == "... --- ..."
    assert text_to_morse("CIAO") == "-.-. .. .- ---"


def test_morse_to_text():
    assert morse_to_text("... --- ...") == "SOS"
    assert morse_to_text("-.-. .. .- ---") == "CIAO"
