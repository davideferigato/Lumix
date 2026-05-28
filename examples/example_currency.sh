#!/bin/bash

# Esempi di conversioni valutarie con lumix CLI

echo "EUR → USD"
lumix --type currency --from EUR --to USD 50

echo "USD → JPY"
lumix --type currency --from USD --to JPY 10

echo "GBP → CHF"
lumix --type currency --from GBP --to CHF 20

# Esempio con localizzazione italiana
echo "Localizzazione italiana"
LANG=it lumix --tipo currency --da EUR --a USD 15
