import os
import datetime

def list_files(path="."):
    try:
        return "\n".join(os.listdir(path))
    except Exception as e:
        return f"Erro ao listar arquivos: {e}"

def current_time():
    return f"Hora atual: {datetime.datetime.now()}"

def read_text_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Não foi possível ler o arquivo: {e}"
