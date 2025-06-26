# config.py

import os
from colorama import Fore, Style, init

init() # Inicializa o Colorama

# --- Constantes para cores Colorama ---
VERDE = Fore.GREEN
VERMELHO = Fore.RED
AZUL = Fore.BLUE
AMARELO = Fore.YELLOW
CIANO = Fore.CYAN
RESET = Style.RESET_ALL

# --- Constantes para nomes de arquivos ---
ARQUIVO_PERGUNTAS = "perguntas.json"
ARQUIVO_RANKING = "ranking.json"