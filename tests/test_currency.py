from unittest.mock import patch

from lumix.currency.convert import convert_currency


# Il mock deve colpire il punto esatto in cui la funzione viene usata: dentro il modulo convert
@patch("lumix.currency.convert.fetch_exchange_rate")
def test_convert_currency(mock_fetch):
    # Simula il tasso di cambio: per 100 EUR → USD restituisce 118.0
    mock_fetch.return_value = 118.0

    converted = convert_currency(100, "EUR", "USD")
    assert converted == 118.0

    # Test con valute uguali
    assert convert_currency(50, "EUR", "EUR") == 50.0
