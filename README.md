# Jogo Educativo Multicultural - Desafio Jovem Programador SENAC/SC

Este projeto foi desenvolvido como parte do **Hackathon ADS** da Semana Acadêmica do **Programa Jovem Programador do SENAC/SC**, com o tema **"A Internacionalização da Educação Superior"**. O objetivo foi criar um jogo educativo em formato de quiz interativo que promove o conhecimento sobre culturas, idiomas e sistemas educacionais globais.

---

## 🎮 Sobre o Jogo

O **Jogo Educativo Multicultural** é um quiz interativo baseado em terminal, projetado para desafiar e educar jogadores sobre a diversidade do nosso mundo. Os jogadores respondem a perguntas de múltipla escolha sobre diferentes culturas, idiomas e modelos educacionais. A cada resposta correta, a pontuação aumenta, incentivando o aprendizado ativo e a competição saudável através de um sistema de ranking.

### 🎯 Objetivo do Jogo

O principal objetivo é que os jogadores aprendam e se divirtam, explorando curiosidades e fatos importantes sobre a internacionalização da educação e a riqueza cultural global.

### 📚 Tópicos Abordados

As perguntas do quiz cobrem uma ampla gama de conhecimentos, incluindo:

* **Cultura:** Práticas culturais, festivais, costumes e tradições ao redor do mundo.
* **Idioma:** Diferenças linguísticas, expressões culturais e vocabulário específico de diversos países.
* **Sistemas Educacionais:** Estruturas de ensino, modelos educacionais em diferentes países e curiosidades sobre universidades globais.

---

## ✨ Recursos e Funcionalidades

O jogo foi desenvolvido com foco em interatividade, aprendizado e acessibilidade:

1.  **Perguntas e Respostas:**
    * Questões de múltipla escolha com 4 alternativas.
    * Exemplos de perguntas: "Qual é o idioma oficial do Japão?", "Como funciona o sistema de educação na Alemanha?", "Quais são as tradições do Dia dos Mortos no México?".
2.  **Ranking e Pontuação:**
    * Sistema de pontuação onde respostas corretas aumentam o total do jogador.
    * Um ranking persistente registra as melhores pontuações, promovendo uma competição amigável.
3.  **Interatividade:**
    * Interface de terminal simples e gamificada.
    * **Animações e Transições:** Utilização de cores e efeitos visuais básicos para tornar a experiência mais envolvente.
    * **Feedback Imediato:** Após cada pergunta, o jogador recebe feedback instantâneo, com a explicação da resposta correta e contextualização da informação, facilitando o aprendizado ativo.
4.  **Multilinguismo:**
    * O jogo oferece suporte a diferentes versões linguísticas (atualmente Português e Inglês), demonstrando o conceito de internacionalização e acessibilidade global.
5.  **Desafios Culturais (Bônus):**
    * Mini-jogos interativos planejados para futuras implementações, podendo incluir desafios como "montar" uma bandeira com peças virtuais.

---

## 🛠️ Instalação e Execução

Para rodar o **Jogo Educativo Multicultural** em sua máquina, siga os passos abaixo:

### Pré-requisitos

* **Python 3.x** (Recomendado Python 3.8 ou superior)

### Passo a Passo

1.  **Clone o Repositório (ou baixe os arquivos):**
    Se você tiver o Git instalado, use o comando:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO] # Substitua pela URL do seu repositório
    cd desafio_hack1
    ```
    Caso contrário, baixe o arquivo ZIP do projeto e descompacte-o em uma pasta de sua escolha. Navegue até essa pasta via terminal (Ex: `cd C:\caminho\para\desafio_hack1`).

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    É uma boa prática criar um ambiente virtual para gerenciar as dependências do projeto.
    ```bash
    python -m venv venv
    ```
    Para ativar o ambiente virtual:
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as Dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas necessárias. As dependências são listadas no `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Jogo:**
    Certifique-se de que você está dentro da pasta principal do projeto (`desafio_hack1`) no terminal e com o ambiente virtual ativado.
    ```bash
    python main.py
    ```
    O jogo iniciará no terminal, permitindo que você escolha o idioma e comece a jogar.

---

## 📦 Estrutura do Projeto

O projeto é organizado em módulos para facilitar a manutenção e a expansão:
