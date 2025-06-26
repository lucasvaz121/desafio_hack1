# question_manager.py
import json
import os
from config import VERMELHO, RESET, ARQUIVO_PERGUNTAS # Importação absoluta
# ...

def carregar_perguntas(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"{VERMELHO}Erro:{RESET} O arquivo de perguntas '{caminho_arquivo}' não foi encontrado.")
        return []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            perguntas_carregadas = json.load(f)
            if not isinstance(perguntas_carregadas, list):
                print(f"{VERMELHO}Erro:{RESET} O arquivo '{caminho_arquivo}' não contém uma lista de perguntas válida.")
                return []
            return perguntas_carregadas
    except json.JSONDecodeError:
        print(f"{VERMELHO}Erro:{RESET} O arquivo '{caminho_arquivo}' está mal formatado (JSON inválido).")
        return []
    except Exception as e:
        print(f"{VERMELHO}Erro inesperado ao carregar perguntas: {e}{RESET}")
        return []