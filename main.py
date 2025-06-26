# main.py
import sys

from quiz_logic import jogar_quiz
from config import AMARELO, VERMELHO, AZUL, RESET

if __name__ == "__main__":
    while True:
        # Chama a função principal do quiz
        jogo_concluido = jogar_quiz()

        # Só pergunta se quer jogar novamente se o quiz foi concluído com sucesso
        if jogo_concluido:
            # Loop interno para garantir uma resposta válida (s ou n)
            while True:
                jogar_novamente_input = input(f"\n{AZUL}Quer jogar novamente? (s/n):{RESET} ").strip().lower()
                
                match jogar_novamente_input:
                    case "s":
                        # Se 's', o loop interno termina e o loop externo continua (reinicia o jogo)
                        break 
                    case "n":
                        print(f"\n{AMARELO}Obrigado por jogar! Até a próxima!{RESET}")
                        sys.exit() # Usar sys.exit() é mais explícito para encerrar o programa
                    case _: # Padrão coringa para qualquer outra entrada
                        print(f"{VERMELHO}Opção não reconhecida. Por favor, digite 's' para sim ou 'n' para não.{RESET}")
                        # O loop interno continua, pedindo a entrada novamente
        else:
            # Se o quiz não pôde ser iniciado (ex: arquivo de perguntas ausente), encerra o programa
            print(f"\n{VERMELHO}Não foi possível iniciar o quiz. Encerrando o programa.{RESET}")
            sys.exit() # Usar sys.exit() aqui também para garantir o encerramento