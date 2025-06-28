# desafio_hack1
#Importação de biblioteca:
import random

Definição das perguntas:
perguntas = [ {...}, {...}, {...} ]
Lista de dicionários, onde cada dicionário contém:
pergunta: o enunciado da pergunta.
opcoes: lista com 4 opções de resposta.
resposta: a opção correta.
explicacao: justificativa educativa da resposta.

Pontuação inicial:
pontuacao = 0

Mensagem de boas-vindas e embaralhamento:
print("Bem-vindo ao Quiz Educativo Multicultural!\n")
random.shuffle(perguntas)

Laço principal (for) para cada pergunta:
for pergunta in perguntas:
Itera por todas as perguntas da lista.

Exibição da pergunta e opções:
print(pergunta["pergunta"])
for i, opcao in enumerate(pergunta["opcoes"], start=1):
    print(f"{i}. {opcao}")
Mostra a pergunta e enumera as opções (1 a 4).

Entrada do utilizador e verificação:
resposta = input("Escolhe uma opção (1-4): ")
if pergunta["opcoes"][int(resposta)-1] == pergunta["resposta"]:
    pontuacao += 10
Recebe a resposta do utilizador, compara com a correta e adiciona pontos se acertar.

Mostrar explicação e pontuação:
print("Explicação:", pergunta["explicacao"])
print("Pontuação atual:", pontuacao)
Exibe a explicação educativa e a pontuação atual.

Encerramento do quiz:
print(f"Quiz concluído! Pontuação final: {pontuacao} pontos")
Informa a pontuação final e agradece.
