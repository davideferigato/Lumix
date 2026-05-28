# Base image con Python 3
FROM python:3.11-slim

# Imposta directory di lavoro
WORKDIR /app

# Copia file del progetto
COPY . .

# Installa le dipendenze dichiarate nel pyproject.toml
RUN pip install --upgrade pip \
 && pip install .

# Comando di default (può essere sovrascritto all'esecuzione)
ENTRYPOINT ["lumix"]
CMD ["--help"]
