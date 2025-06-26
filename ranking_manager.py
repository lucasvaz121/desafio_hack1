# ranking_manager.py
import json
import os
from config import VERMELHO, CIANO, AMARELO, VERDE, RESET, ARQUIVO_RANKING 
def carregar_ranking():
    if not os.path.exists(ARQUIVO_RANKING): # ARQUIVO_RANKING precisa ser importado ou passado
        return []
    try:
        with open(ARQUIVO_RANKING, 'r', encoding='utf-8') as f:
            ranking = json.load(f)
            if not isinstance(ranking, list):
                return []
            return ranking
    except json.JSONDecodeError:
        print(f"{VERMELHO}Aviso:{RESET} Arquivo '{ARQUIVO_RANKING}' corrompido. Criando um novo ranking.")
        return []
    except Exception as e:
        print(f"{VERMELHO}Erro ao carregar o ranking: {e}{RESET}")
        return []

def salvar_ranking(ranking):
    try:
        with open(ARQUIVO_RANKING, 'w', encoding='utf-8') as f:
            json.dump(ranking, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"{VERMELHO}Erro ao salvar o ranking: {e}{RESET}")

def exibir_ranking(ranking):
    print(f"\n{AMARELO}┏━━ RANKING DOS MELHORES JOGADORES ━━┓{RESET}")
    if not ranking:
        print(f"{CIANO}Nenhuma pontuação registrada ainda.{RESET}")
        return

    ranking_ordenado = sorted(ranking, key=lambda x: x['pontuacao'], reverse=True)

    for i, jogador in enumerate(ranking_ordenado[:10]):
        print(f" {i + 1}. {jogador['nome']} - {VERDE}{jogador['pontuacao']}{RESET} pontos")
    print(f"{AMARELO}━" * 38 + RESET)

# Para que ARQUIVO_RANKING esteja disponível aqui, ele precisa ser importado
# ou você pode passar como argumento para as funções.
# A melhor forma é importar:
from config import ARQUIVO_RANKING