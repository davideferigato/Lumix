"""
Funzioni per convertire numeri in parole in diverse lingue.
"""


def number_to_words_en(n: int) -> str:
    """Converte un intero in parole in inglese."""
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    thousands = ["", "thousand", "million", "billion"]

    if n == 0:
        return "zero"

    def helper(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            ten = tens[num // 10]
            rest = helper(num % 10)
            return ten + ("-" + rest if rest else "")
        else:
            hundred = ones[num // 100] + " hundred"
            rest = helper(num % 100)
            return hundred + (" " + rest if rest else "")

    result = []
    i = 0
    while n > 0:
        chunk = n % 1000
        if chunk:
            chunk_str = helper(chunk)
            if thousands[i]:
                chunk_str += " " + thousands[i]
            result.append(chunk_str)
        n //= 1000
        i += 1
    return " ".join(reversed(result))


# noqa: C901
def number_to_words_it(n: int) -> str:  # noqa: C901  # noqa: C901
    """Converte un intero in parole in italiano."""
    ones = [
        "",
        "uno",
        "due",
        "tre",
        "quattro",
        "cinque",
        "sei",
        "sette",
        "otto",
        "nove",
    ]
    teens = [
        "dieci",
        "undici",
        "dodici",
        "tredici",
        "quattordici",
        "quindici",
        "sedici",
        "diciassette",
        "diciotto",
        "diciannove",
    ]
    tens = [
        "",
        "",
        "venti",
        "trenta",
        "quaranta",
        "cinquanta",
        "sessanta",
        "settanta",
        "ottanta",
        "novanta",
    ]
    hundreds = [
        "",
        "cento",
        "duecento",
        "trecento",
        "quattrocento",
        "cinquecento",
        "seicento",
        "settecento",
        "ottocento",
        "novecento",
    ]
    thousands = ["", "mila", "milioni", "miliardi"]

    if n == 0:
        return "zero"

    def helper(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            ten = tens[num // 10]
            rest = helper(num % 10)
            # gestione delle eccezioni: ventuno, ventotto, trentuno, ecc.
            if rest and (ten.endswith("i") or ten.endswith("a")):
                if rest in ("uno", "otto"):
                    ten = ten[:-1] + rest[0]  # venti + uno -> ventuno
                else:
                    ten = ten + rest
                return ten
            else:
                return ten + (" " + rest if rest else "")
        else:
            hundred = hundreds[num // 100]
            rest = helper(num % 100)
            return hundred + (" " + rest if rest else "")

    result = []
    i = 0
    while n > 0:
        chunk = n % 1000
        if chunk:
            chunk_str = helper(chunk)
            if thousands[i]:
                # gestione "mila" vs "mille"
                if i == 1 and chunk == 1:
                    chunk_str = "mille"
                else:
                    chunk_str += " " + thousands[i]
            result.append(chunk_str)
        n //= 1000
        i += 1
    return " ".join(reversed(result))


def number_to_words_fr(n: int) -> str:
    """Converte un intero in parole in francese (versione semplificata)."""
    # Implementazione di base, da completare se necessario
    return f"[FR] {n}"


def number_to_words_es(n: int) -> str:
    """Converte un intero in parole in spagnolo (versione semplificata)."""
    return f"[ES] {n}"


def number_to_words_jp(n: int) -> str:
    """Converte un intero in parole in giapponese (versione semplificata)."""
    return f"[JP] {n}"


def number_to_words(n: int, lang: str = "en") -> str:
    """
    Converte un numero intero in parole nella lingua specificata.
    """
    lang = lang.lower()
    if lang == "en":
        return number_to_words_en(n)
    elif lang == "it":
        return number_to_words_it(n)
    elif lang == "fr":
        return number_to_words_fr(n)
    elif lang == "es":
        return number_to_words_es(n)
    elif lang == "jp":
        return number_to_words_jp(n)
    else:
        raise ValueError(f"Lingua non supportata: {lang}")
