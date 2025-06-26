import random
pontuacao = 0


def menu_jogo():
    print("=" * 32)
    print("          Menu do Jogo")
    print("=" * 32)
    print("[1] - Jogar.")
    print("[2] - Visualizar pontuação.")
    print("[3] - Sair")
    return input("Insira a opção que deseja executar: ")
while True:
    print("\n")
    opcao = menu_jogo()
    print("\n")
    match opcao:
        case "1":
            perguntas = [
                {
                    "pergunta": """
            ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜⬜🔴🔴⬜⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜🔴🔴🔴🔴⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜🔴🔴🔴🔴🔴🔴⬜⬜⬜⬜
            ⬜⬜⬜⬜🔴🔴🔴🔴🔴🔴⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜🔴🔴🔴🔴⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜⬜🔴🔴⬜⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\nQual é o idioma oficial do Japão?""",
                    "opcoes": ["Chinês", "Coreano", "Japonês", "Tailandês"],
                    "resposta": "Japonês",
                    "explicacao": "O idioma oficial do Japão é o japonês, falado por mais de 125 milhões de pessoas."
                },
                {
                    "pergunta": """
            🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
            🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
            🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
            🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
            🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
            🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
            🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
            🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
            🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\nComo funciona o sistema de educação na Alemanha?""",
                    "opcoes": [
                        "Ensino único até à universidade",
                        "Divisão em três vias após o ensino básico",
                        "Só escolas privadas",
                        "Educação somente em tempo integral"
                    ],
                    "resposta": "Divisão em três vias após o ensino básico",
                    "explicacao": "Na Alemanha, os alunos são divididos em três tipos de escolas secundárias com base no desempenho."
                },
                {
                    "pergunta": """
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
                    \nQuais são as tradições do Dia dos Mortos no México?""",
                    "opcoes": [
                        "Festas com fogos de artifício",
                        "Culto às árvores",
                        "Altares com oferendas e visitas ao cemitério",
                        "Jejum e silêncio"
                    ],
                    "resposta": "Altares com oferendas e visitas ao cemitério",
                    "explicacao": "O Dia dos Mortos no México é celebrado com altares decorados, oferendas e visitas aos túmulos dos entes queridos."
                }
            ]

            print("Bem-vindo ao Quiz Educativo Multicultural!")
            random.shuffle(perguntas)

            for pergunta in perguntas:
                print(pergunta["pergunta"])
                for i, opcao in enumerate(pergunta["opcoes"], start=1):
                    print(f"{i}. {opcao}")

                resposta = input("Escolhe uma opção (1-4): ")
                if pergunta["opcoes"][int(resposta)-1] == pergunta["resposta"]:
                    print("\n Resposta correta!")
                    pontuacao += 10
                else:
                    print("\n Resposta incorreta.")
                    pontuacao -= 5
                print("Explicação:", pergunta["explicacao"])
                print("Pontuação atual:", pontuacao)
                print("\n" + "-"*40 + "\n")

            print(f"Quiz concluído! Pontuação final: {pontuacao} pontos")
            print("Obrigado por jogar! ")
        case "2":
            print(f"Sua pontuação no momento é {pontuacao}")
        
        case "3":
            break