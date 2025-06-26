import random
pontuacao = 0
idioma = "PTBR"

perguntas = {
    "PTBR": [
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
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥\nQuais são as tradições do Dia dos Mortos no México?""",
            "opcoes": [
                "Festas com fogos de artifício",
                "Culto às árvores",
                "Altares com oferendas e visitas ao cemitério",
                "Jejum e silêncio"
            ],
            "resposta": "Altares com oferendas e visitas ao cemitério",
            "explicacao": "O Dia dos Mortos no México é celebrado com altares decorados, oferendas e visitas aos túmulos dos entes queridos."
        }
    ],
    "en": [
        {
            "pergunta": """
            ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜⬜🔴🔴⬜⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜🔴🔴🔴🔴⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜🔴🔴🔴🔴🔴🔴⬜⬜⬜⬜
            ⬜⬜⬜⬜🔴🔴🔴🔴🔴🔴⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜🔴🔴🔴🔴⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜⬜🔴🔴⬜⬜⬜⬜⬜⬜
            ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\nWhat is the official language of Japan?""",
            "opcoes": ["Chinese", "Korean", "Japanese", "Thai"],
            "resposta": "Japanese",
            "explicacao": "The official language of Japan is Japanese, spoken by over 125 million people."
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
            🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\nHow does the education system work in Germany?""",
            "opcoes": [
                "Single system until university",
                "Division into three paths after basic education",
                "Only private schools",
                "Full-time education only"
            ],
            "resposta": "Division into three paths after basic education",
            "explicacao": "In Germany, students are divided into three types of secondary schools based on performance."
        },
        {
            "pergunta": """
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥
            🟩🟩🟩🟩🟩🟩 ⬜⬜⬜⬜⬜⬜ 🟥🟥🟥🟥🟥🟥\nWhat are the traditions of the Day of the Dead in Mexico?""",
            "opcoes": [
                "Fireworks parties",
                "Tree worship",
                "Altars with offerings and cemetery visits",
                "Fasting and silence"
            ],
            "resposta": "Altars with offerings and cemetery visits",
            "explicacao": "The Day of the Dead in Mexico is celebrated with decorated altars, offerings and visits to the graves of loved ones."
        }
    ]
}

def quiz():
    global pontuacao
    perguntas_atuais = perguntas[idioma]
    random.shuffle(perguntas_atuais)

    if idioma == "PTBR":
        print("Bem-vindo ao Quiz Educativo Multicultural!")
    else:
        print("Welcome to the Multicultural Educational Quiz!")

    for pergunta in perguntas_atuais:
        print(pergunta["pergunta"])
        for i, opcao in enumerate(pergunta["opcoes"], start=1):
            print(f"{i}. {opcao}")

        resposta = input(f"{'Escolha uma opção' if idioma == 'PTBR' else 'Choose an option'} (1-4): ")
        
        try:
            if pergunta["opcoes"][int(resposta)-1] == pergunta["resposta"]:
                print("\n✓ Correct!" if idioma == "en" else "\n✓ Resposta correta!")
                pontuacao += 10
            else:
                print("\n✗ Incorrect!" if idioma == "en" else "\n✗ Resposta incorreta.")
                pontuacao -= 5
        except (IndexError, ValueError):
            print("\n⚠ Invalid option! No points." if idioma == "en" else "\n⚠ Opção inválida! Sem pontos.")

        print(f"{'Explanation' if idioma == 'en' else 'Explicação'}: {pergunta['explicacao']}")
        print(f"{'Current score' if idioma == 'en' else 'Pontuação atual'}: {pontuacao}")
        print("\n" + "-"*40 + "\n")

    if idioma == "PTBR":
        print(f"Quiz concluído! Pontuação final: {pontuacao} pontos")
        print("Voltando para o menu!")
    else:
        print(f"Quiz completed! Final score: {pontuacao} points")
        print("Returning to the menu!")

def menu_jogo():
    print("=" * 32)
    if idioma == "PTBR":
        print("          Menu do Jogo")
        print("=" * 32)
        print("[1] - Jogar.")
        print("[2] - Visualizar pontuação.")
        print("[3] - Mudar para Inglês")
        print("[4] - Sair")
        return input("Insira a opção que deseja executar: ")
    else:
        print("          Game Menu")
        print("=" * 32)
        print("[1] - Play")
        print("[2] - View score")
        print("[3] - Switch to Portuguese")
        print("[4] - Exit")
        return input("Enter your choice: ")

while True:
    print("\n")
    opcao = menu_jogo()
    print("\n")
    match opcao:
        case "1":
            quiz()

        case "2":
            if idioma == "PTBR":
                print(f"Sua pontuação no momento é {pontuacao}")
            else:
                print(f"Your current score is {pontuacao}")
        
        case "3":
            idioma = "en" if idioma == "PTBR" else "PTBR"
            if idioma == "PTBR":
                print("Idioma alterado para Português Brasil")
            else:
                print("Language changed to English")

        case "4":
            if idioma == "PTBR":
                print("Obrigado por jogar! Até logo!")
                print("\n")

            else:
                print("Thank you for playing! Goodbye!")
                print("\n")
                
            break

        case _:
            if idioma == "PTBR":
                print("Opção inválida. Por favor, tente novamente.")
            else:
                print("Invalid option. Please try again.")
