import random

perguntas = [
    {
        "pergunta": "Qual é o idioma oficial do Japão?",
        "opcoes": ["Chinês", "Coreano", "Japonês", "Tailandês"],
        "resposta": "Japonês",
        "explicacao": "O idioma oficial do Japão é o japonês, falado por mais de 125 milhões de pessoas."
    },
    {
        "pergunta": "Como funciona o sistema de educação na Alemanha?",
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
        "pergunta": "Quais são as tradições do Dia dos Mortos no México?",
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

pontuacao = 0

print("Bem-vindo ao Quiz Educativo Multicultural!\n")
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
    print("Explicação:", pergunta["explicacao"])
    print("Pontuação atual:", pontuacao)
    print("\n" + "-"*40 + "\n")

print(f"Quiz concluído! Pontuação final: {pontuacao} pontos")
print("Obrigado por jogar! ")