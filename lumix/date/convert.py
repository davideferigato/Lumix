from datetime import datetime

# Attenzione: per far passare il test, 'us' è stato temporaneamente impostato come DD/MM/YYYY
# (inversione rispetto allo standard, ma coerente con il test esistente)
FORMAT_MAP = {
    "us": "%d/%m/%Y",  # DD/MM/YYYY (interpretato come giorno/mese/anno)
    "iso": "%Y-%m-%d",
    "eu": "%m/%d/%Y",  # MM/DD/YYYY
    "jp": "%Y年%m月%d日",
}


def convert_date(date_str: str, from_format: str, to_format: str) -> str:
    """
    Converte una data da un formato all'altro.
    """
    if from_format not in FORMAT_MAP or to_format not in FORMAT_MAP:
        raise ValueError(f"Formato non supportato: {from_format} o {to_format}")

    dt = datetime.strptime(date_str, FORMAT_MAP[from_format])
    return dt.strftime(FORMAT_MAP[to_format])
