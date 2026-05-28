#!/bin/bash

# Esempi di conversioni tra basi numeriche con lumix CLI

echo "DEC → BIN"
lumix --type base --from dec --to bin 42

echo "BIN → DEC"
lumix --type base --from bin --to dec 101010

echo "DEC → HEX"
lumix --type base --from dec --to hex 255

echo "HEX → DEC"
lumix --type base --from hex --to dec ff

echo "DEC → OCT"
lumix --type base --from dec --to oct 64

echo "OCT → DEC"
lumix --type base --from oct --to dec 100
