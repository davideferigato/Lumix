#!/bin/bash
# Esempi codice Morse
echo "Testo 'SOS' → Morse:"
lumix en morse from-text "SOS"
echo "Morse '... --- ...' → testo:"
lumix en morse to-text "... --- ..."

