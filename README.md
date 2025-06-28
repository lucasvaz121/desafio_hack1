🧩 1. Importações e Variáveis Iniciais
import random
pontuacao = 0
idioma = "PTBR"
random é usado para embaralhar as perguntas.
pontuacao começa em zero.
idioma define o idioma padrão do jogo como Português Brasil (PTBR).

📚 2. Base de Dados das Perguntas
perguntas = {
    "PTBR": [...],
    "en": [...]
}
Dicionário com perguntas organizadas por idioma: PTBR e en (inglês).
Cada pergunta inclui:
pergunta com arte em blocos e o texto;
opcoes com 4 alternativas;
resposta correta;
explicacao para aprendizado.

🎮 3. Função quiz()
def quiz():
    ...
Embaralha as perguntas do idioma atual.
Dá boas-vindas dependendo do idioma.
Para cada pergunta:
Mostra o enunciado e opções.
Recebe resposta do jogador.
Verifica se está certa:
Acerta: +10 pontos;
Erra: -5 pontos;
Inválida: 0 pontos.
Mostra explicação e pontuação atual.
Ao fim, mostra a pontuação final.

📋 4. Função menu_jogo()
def menu_jogo():
    ...
    Exibe o menu principal com opções, conforme o idioma atual:
[1] Jogar;
[2] Ver pontuação;
[3] Trocar idioma (PTBR/inglês);
[4] Sair do jogo.

🔁 5. Loop Principal
while True:
    ...
    match opcao:
        ...
Mostra o menu, recebe a opção e executa:
"1" → chama quiz();
"2" → mostra pontuação atual;
"3" → troca entre PTBR e en;
"4" → encerra o jogo;
Qualquer outro valor → mensagem de erro.

✅ Destaques Especiais
Suporte a dois idiomas com o mesmo código.
Mensagens, perguntas e respostas se ajustam automaticamente ao idioma.
Feedback imediato e educativo após cada pergunta.
Interface com blocos coloridos 🟩🟥⬜ para atrair atenção visual.





