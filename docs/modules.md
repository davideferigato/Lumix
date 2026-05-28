
---

## **`docs/modules.md`** (Riferimento Completo dei Moduli)

```markdown
# Moduli di `lumix` – Riferimento Completo

Questo documento elenca tutti i moduli disponibili, le unità supportate, le opzioni specifiche e la sintassi dettagliata.

---

## Convenzioni

- **Lingua**: primo argomento (`en`, `it`, `fr`, `es`, `jp`).
- **Tipo**: secondo argomento, corrisponde alla tabella in `usage.md`.
- **Parametri**: variano per modulo, ma generalmente:
  - `from <unità> to <unità> <valore>` (inglese)
  - `da <unità> a <unità> <valore>` (italiano)
  - ecc.

---

## Moduli di Conversione Fisica

### `temps` (Temperatura)
- **Unità**: `C`, `F`, `K`
- **Sintassi**: `<lang> temperature from <unità> to <unità> <valore>`
- **Esempio**: `en temperature from C to F 36.5`

### `weight` (Peso/Massa)
- **Unità**: `g`, `kg`, `lb`, `oz`, `mg`, `st` (stone), `t` (tonnellata)
- **Sintassi**: `<lang> weight from <unità> to <unità> <valore>`

### `length` (Lunghezza)
- **Unità**: `m`, `km`, `cm`, `mm`, `mi`, `yd`, `ft`, `in`, `nmi`
- **Sintassi**: `<lang> length from <unità> to <unità> <valore>`

### `volume` (Volume)
- **Unità**: `l`, `ml`, `m3`, `gal` (US), `qt`, `pt`, `cup`, `fl oz`, `uk gal` (imperiale)
- **Sintassi**: `<lang> volume from <unità> to <unità> <valore>`

### `area` (Superficie)
- **Unità**: `m2`, `km2`, `ft2`, `mi2`, `ha`, `acre`, `cm2`, `mm2`, `yd2`, `in2`
- **Sintassi**: `<lang> area from <unità> to <unità> <valore>`

### `speed` (Velocità)
- **Unità**: `km/h`, `mph`, `m/s`, `kn` (knot)
- **Sintassi**: `<lang> speed from <unità> to <unità> <valore>`

### `time` (Tempo)
- **Unità**: `s` (secondi), `min` (minuti), `h` (ore), `d` (giorni), `w` (settimane)
- **Sintassi**: `<lang> time from <unità> to <unità> <valore>`

### `energy` (Energia)
- **Unità**: `J`, `kJ`, `cal`, `kcal`, `Wh`, `kWh`, `eV`
- **Sintassi**: `<lang> energy from <unità> to <unità> <valore>`

### `pressure` (Pressione)
- **Unità**: `Pa`, `bar`, `atm`, `mmHg`, `psi`
- **Sintassi**: `<lang> pressure from <unità> to <unità> <valore>`

### `power` (Potenza)
- **Unità**: `W`, `kW`, `hp` (cavallo vapore meccanico)
- **Sintassi**: `<lang> power from <unità> to <unità> <valore>`

---

## Moduli di Utilità Digitale

### `data` (Dati digitali)
- **Unità**: `B`, `KB`, `MB`, `GB`, `TB` (base 1024)
- **Sintassi**: `<lang> data from <unità> to <unità> <valore>`

### `bitrate` (Bitrate)
- **Unità**: `bps`, `kbps`, `Mbps`, `Gbps`, `Tbps` (base 1000)
- **Sintassi**: `<lang> bitrate from <unità> to <unità> <valore>`

### `hash` (Hash)
- **Algoritmi**: `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`
- **Sintassi**: `<lang> hash <algoritmo> <stringa>`

### `color` (Colori)
- **Sintassi**:
  - `from rgb to hex <r,g,b>`   (es. `255,255,255`)
  - `from hex to rgb <#RRGGBB>`  (es. `#ff0000` o `ff0000`)

### `iptools` (Strumenti IP)
- **Comandi**:
  - `cidr-to-range <cidr>`       (es. `192.168.1.0/24`)
  - `ip-to-bin <ip>`              (es. `192.168.1.1`)
  - `bin-to-ip <binario>`         (32 bit con o senza punti)
  - `netmask <cidr>`              (es. `192.168.1.0/24`)
  - `subnet-info <cidr>`          (mostra rete, maschera, broadcast, host, wildcard)

---

## Moduli di Data e Tempo

### `timezones` (Fusi orari)
- **Sintassi**: `<lang> timezones from <fuso> to <fuso> <data_ora>`
- **Formati data**: dipendono dalla lingua (ISO, EU, US, JP)

### `date` (Formati data)
- **Formati**: `us` (MM/DD/YYYY), `iso` (YYYY-MM-DD), `eu` (DD/MM/YYYY), `jp` (YYYY年MM月DD日)
- **Sintassi**: `<lang> date from <formato> to <formato> <data>`

### `calendar` (Differenza date)
- **Sintassi**: `<lang> calendar diff <data1> <data2>`

### `age` (Calcolo età)
- **Sintassi**: `<lang> age from <data_di_nascita>`

---

## Moduli di Sicurezza e Crittografia

### `passwords` (Generazione password)
- **Sintassi**: `<lang> passwords generate length <N> [symbols true|false]`

---

## Moduli Geo, Lingue, Codici

### `country` (Paesi)
- **Sintassi**:
  - `from code to name <codice>`   (es. `IT`)
  - `from name to code <nome>`     (es. `Italy`)

### `language` (Lingue)
- **Sintassi**:
  - `from code to name <codice>`   (es. `en`)
  - `from name to code <nome>`     (es. `Italian`)

### `unitsymbols` (Simboli unità)
- **Sintassi**: `<lang> unitsymbols from <simbolo|nome> to <"unit name"|"symbol"|"type">`
- **Esempio**: `en unitsymbols from W to "unit name"` → `watt`

---

## Moduli Bonus Creativi

### `roman` (Numeri romani)
- **Sintassi**:
  - `from <numero_arabo>`   (es. `2025`)
  - `to <numero_romano>`    (es. `MMXXV`)

### `morse` (Codice Morse)
- **Sintassi**:
  - `from-text <testo>`      (testo → Morse)
  - `to-text <codice_morse>` (Morse → testo)

### `timezonebot` (Ora in una città)
- **Sintassi**: `<lang> timezonebot what-time <città>`
- **Database**: oltre 100 città mondiali mappate ai fusi IANA.

### `spoken` (Numeri in parole)
- **Sintassi**: `<lang> spoken from <numero>`
- **Lingue**: inglese (completo), italiano (completo), francese/spagnolo/giapponese (implementazione base)

### `phonetic` (Alfabeto fonetico NATO)
- **Sintassi**: `<lang> phonetic for <testo>`
- **Mappa**: lettere A-Z e cifre 0-9.

---

## Note Implementative

- Ogni modulo è indipendente e può essere esteso/modificato senza impattare gli altri.
- I parser gestiscono la localizzazione delle parole chiave e la validazione degli input.
- I test unitari per ogni modulo sono in `tests/test_<modulo>.py`.
- Per aggiungere un nuovo modulo, creare una nuova cartella con `__init__.py`, `convert.py`, `parser.py` e aggiornare la mappa `PARSER_MODULES` in `cli/main.py`.
