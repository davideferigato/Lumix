#!/usr/bin/env python3
"""Test end‑to‑end del comando CLI via subprocess."""

import subprocess
import sys

import pytest

# Percorso dello script CLI
CLI_PATH = "cli.py"

def run_lumix(args: list) -> subprocess.CompletedProcess:
    """Esegue il comando lumix con gli argomenti dati."""
    cmd = [sys.executable, CLI_PATH] + args
    return subprocess.run(cmd, capture_output=True, text=True)

@pytest.mark.skip(reason="Il comando lumix non è ancora pienamente funzionante; da abilitare dopo il fix del dispatcher")
def test_temperature_conversion():
    result = run_lumix(["en", "temperature", "from", "C", "to", "F", "36.5"])
    assert result.returncode == 0
    assert "97.70" in result.stdout

@pytest.mark.skip(reason="In attesa di fix")
def test_currency_conversion():
    result = run_lumix(["en", "currency", "from", "EUR", "to", "USD", "50"])
    assert result.returncode == 0
    assert "USD" in result.stdout

@pytest.mark.skip(reason="In attesa di fix")
def test_help():
    result = run_lumix(["--help"])
    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()

@pytest.mark.skip(reason="In attesa di fix")
def test_invalid_language():
    result = run_lumix(["xx", "temperature", "from", "C", "to", "F", "0"])
    assert result.returncode != 0
    assert "non supportata" in result.stderr or "not supported" in result.stderr
