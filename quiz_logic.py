# quiz_logic.py
import random
import os
from config import VERDE, VERMELHO, AZUL, AMARELO, CIANO, RESET, ARQUIVO_PERGUNTAS # Importação absoluta
from ranking_manager import carregar_ranking, salvar_ranking, exibir_ranking # Importação absoluta
from questions_manager import carregar_perguntas # Importação absoluta


def exibir_pergunta(pergunta_data):   
    print(f"{AMARELO}{'━' * 80}{RESET}")
    print(f"{AMARELO}Pergunta:{RESET} {pergunta_data['pergunta']}")
    print(f"{AMARELO}{'━' * 80}{RESET}")
    
    opcoes_originais_embaralhadas = random.sample(pergunta_data['opcoes'], len(pergunta_data['opcoes']))
    
    opcoes_formatadas = []
    for i, opcao in enumerate(opcoes_originais_embaralhadas):
        opcao_formatada = f"{i + 1}. {opcao}"
        print(f"{CIANO}{opcao_formatada}{RESET}")
        opcoes_formatadas.append(opcao_formatada)
        
    return opcoes_formatadas

def obter_resposta_jogador(num_opcoes):
    while True:
        try:
            resposta = input(f"\n{AZUL}Digite o número da sua resposta:{RESET} ")
            escolha = int(resposta)
            if 1 <= escolha <= num_opcoes:
                return escolha
            else:
                print(f"{VERMELHO}Opção inválida.{RESET} Por favor, digite um número entre 1 e {num_opcoes}.")
        except ValueError:
            print(f"{VERMELHO}Entrada inválida. Por favor, digite um número.{RESET}")

def verificar_resposta(escolha_jogador, opcoes_exibidas, resposta_correta, explicacao):
    if escolha_jogador == -1:
        print(f"\n{VERMELHO}Resposta não considerada devido a entrada inválida.{RESET}")
        print(f"{AMARELO}A resposta correta era:{RESET} {resposta_correta}")
        print(f"{CIANO}Explicação:{RESET} {explicacao}")
        return False

    resposta_selecionada_texto = opcoes_exibidas[escolha_jogador - 1].split('. ', 1)[1] 

    if resposta_selecionada_texto == resposta_correta:
        print(f"\n{VERDE}🎉 Resposta CORRETA! 🎉{RESET}")
        print(f"{CIANO}Explicação:{RESET} {explicacao}")
        return True
    else:
        print(f"\n{VERMELHO}😢 Resposta INCORRETA. 😢{RESET}")
        print(f"{AMARELO}A resposta correta era:{RESET} {resposta_correta}")
        print(f"{CIANO}Explicação:{RESET} {explicacao}")
        return False

def jogar_quiz():
    perguntas_do_json = carregar_perguntas(ARQUIVO_PERGUNTAS)
    if not perguntas_do_json:
        print("Não foi possível carregar as perguntas. Encerrando o quiz.")
        return False

    NUM_PERGUNTAS_RODADA = 6 
    
    if len(perguntas_do_json) < NUM_PERGUNTAS_RODADA:
        print(f"{CIANO}Atenção:{RESET} Há menos de {NUM_PERGUNTAS_RODADA} perguntas disponíveis. Usando todas as {len(perguntas_do_json)} perguntas.")
        perguntas_para_jogar = random.sample(perguntas_do_json, len(perguntas_do_json))
    else:
        perguntas_para_jogar = random.sample(perguntas_do_json, NUM_PERGUNTAS_RODADA)

    pontuacao = 0
    print(f"{AMARELO}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
    print(f"{AMARELO}┃ {AZUL}                Bem-vindo ao Quiz Educativo Multicultural!               {AMARELO} ┃{RESET}")
    print(f"{AMARELO}┃ {AZUL}Teste seus conhecimentos sobre culturas, idiomas e sistemas educacionais!{AMARELO} ┃{RESET}")
    print(f"{AMARELO}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")

    ranking_atual = carregar_ranking()
    exibir_ranking(ranking_atual)

    nome_jogador = ""
    while not nome_jogador:
        nome_candidato = input(f"\n{AZUL}Digite seu nome para começar:{RESET} ").strip().title()
        
        if not nome_candidato:
            print(f"{VERMELHO}O nome não pode ser vazio. Por favor, digite seu nome.{RESET}")
            continue
        if len(nome_candidato) < 3:
            print(f"{VERMELHO}O nome deve ter no mínimo 3 caracteres. Por favor, digite seu nome novamente.{RESET}")
            continue
        
        jogador_existente = None
        for jogador in ranking_atual:
            if jogador['nome'].lower() == nome_candidato.lower():
                jogador_existente = jogador
                break
        
        if jogador_existente:
            print(f"\nOlá,{VERDE} {nome_candidato}{RESET}! Encontrei você no ranking com {jogador_existente['pontuacao']} pontos.")
            confirmacao = input(f"{AZUL}É você mesmo? (s/n):{RESET} ").strip().lower()
            if confirmacao == 's':
                nome_jogador = nome_candidato
            else:
                print(f"{VERMELHO}Ok, por favor, digite outro nome ou o nome correto.{RESET}")
        else:
            nome_jogador = nome_candidato
            print(f"Bem-vindo,{VERDE} {nome_jogador}{RESET}! Boa sorte no quiz!")

    for i, pergunta_atual in enumerate(perguntas_para_jogar):
        print(f"\n{AMARELO}━━━ Pergunta {i + 1} de {len(perguntas_para_jogar)} ━━━{RESET}")
        opcoes_exibidas = exibir_pergunta(pergunta_atual)
        escolha = obter_resposta_jogador(len(opcoes_exibidas))
        
        resposta_correta_original = pergunta_atual['resposta_correta']

        if verificar_resposta(escolha, opcoes_exibidas, resposta_correta_original, pergunta_atual['explicacao']):
            pontuacao += 10

        input(f"\n{AMARELO}Pressione Enter para continuar...{RESET}")

    print(f"\n{VERMELHO}━━━ FIM DO QUIZ ━━━{RESET}")
    print(f"Sua pontuação final nesta rodada:{VERDE} {pontuacao}{RESET} pontos.")
    print("Obrigado por jogar e aprender!")

    jogador_encontrado_no_fim = False
    for i, jogador in enumerate(ranking_atual):
        if jogador['nome'].lower() == nome_jogador.lower():
            ranking_atual[i]['pontuacao'] += pontuacao
            print(f"Sua nova pontuação total é:{VERDE} {ranking_atual[i]['pontuacao']}{RESET} pontos!")
            jogador_encontrado_no_fim = True
            break
    
    if not jogador_encontrado_no_fim:
        ranking_atual.append({"nome": nome_jogador, "pontuacao": pontuacao})
        print(f"Sua pontuação de {VERDE}{pontuacao}{RESET} pontos foi adicionada ao ranking!")
    
    salvar_ranking(ranking_atual)
    
    exibir_ranking(carregar_ranking())

    return True # Indica que o quiz foi jogado com sucesso