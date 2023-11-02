# Jogo da Cobrinha em Python com Pygame

Bem-vindo ao repositório do **Jogo da Cobrinha**, desenvolvido em Python usando a biblioteca Pygame. Este jogo clássico da cobrinha apresenta uma interface gráfica simples, onde o jogador controla uma cobra que cresce à medida que consome comida, desviando de obstáculos e de seu próprio corpo.

## Como Jogar

- **Setas do Teclado:** Use as setas direcionais para cima, baixo, esquerda e direita para controlar a direção da cobra.
- **Objetivo:** Tente comer a comida (representada em vermelho) para crescer a cobra. Evite colidir com as bordas da tela ou com seu próprio corpo, pois isso encerrará o jogo.

## Estrutura do Código

- **`main.py`**: O arquivo principal contendo a lógica principal do jogo.
- **`Cobra_pulsante.py`**: Um módulo contendo as classes `Food` (representando a comida) e `sanke` (representando a cobra), além da função `drow_tale` para desenhar o corpo da cobra.
- **`pygame`**: A biblioteca Pygame é utilizada para a criação da interface gráfica e controle de eventos do jogo.

## Funcionalidades do Jogo

- **Geração Aleatória de Comida:** A comida é gerada aleatoriamente na tela, proporcionando uma experiência de jogo dinâmica.
- **Crescimento da Cobra:** A cobra cresce à medida que consome a comida, aumentando o desafio à medida que o jogo avança.
- **Verificação de Colisões:** O jogo verifica colisões da cobra com as bordas da tela e com seu próprio corpo, terminando o jogo caso ocorram colisões.
- **Gráficos Simples:** A interface gráfica é apresentada em uma grade simples, facilitando a visualização e a interação.

## Como Executar o Jogo

Para executar o jogo, certifique-se de ter o Python e a biblioteca Pygame instalados em seu sistema. Você pode instalá-lo usando o seguinte comando:

```bash
pip install pygame
```

Após instalar o Pygame, execute o arquivo `main.py` para iniciar o jogo da cobrinha.

```bash
python main.py
```

Divirta-se jogando o Jogo da Cobrinha! 🐍✨
