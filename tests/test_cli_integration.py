import subprocess
import sys

CLI_PATH = "cli.py"


def run_lumix(args):
    cmd = [sys.executable, CLI_PATH] + args
    return subprocess.run(cmd, capture_output=True, text=True)


def test_temperature_conversion():
    result = run_lumix(["en", "temperature", "from", "C", "to", "F", "36.5"])
    assert result.returncode == 0
    assert "97.70" in result.stdout


def test_currency_conversion():
    result = run_lumix(["en", "currency", "from", "EUR", "to", "USD", "50"])
    assert result.returncode == 0
    assert "USD" in result.stdout


def test_help():
    result = run_lumix(["--help"])
    assert result.returncode == 0
    assert "Usage:" in result.stdout


def test_invalid_language():
    result = run_lumix(["xx", "temperature", "from", "C", "to", "F", "0"])
    assert result.returncode != 0
    assert "non riconosciuta" in result.stdout or "not recognized" in result.stdout
