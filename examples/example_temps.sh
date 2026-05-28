

#!/bin/bash

# Esempi di conversioni di temperatura con lumix CLI

echo "Celsius → Fahrenheit"
lumix --type temp --from C --to F 100

echo "Fahrenheit → Celsius"
lumix --type temp --from F --to C 212

echo "Celsius → Kelvin"
lumix --type temp --from C --to K 25

echo "Kelvin → Celsius"
lumix --type temp --from K --to C 298.15

echo "Fahrenheit → Kelvin"
lumix --type temp --from F --to K 32

echo "Kelvin → Fahrenheit"
lumix --type temp --from K --to F 273.15

# Esempio localizzato
echo "Localizzazione in italiano"
LANG=it lumix --tipo temp --da C --a F 37