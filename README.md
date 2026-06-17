# Jogo da Cobrinha em Python com Pygame

Uma versão do clássico **Snake** feita em Python com Pygame, com visuais melhorados e mecânicas de progressão.

## Como Jogar

- Controle a cobra para comer a comida vermelha e crescer
- Evite bater nas bordas ou no próprio corpo
- Quanto mais você come, mais rápido a cobra fica

## Controles

| Tecla | Ação |
|-------|------|
| `W` ou `↑` | Cima |
| `S` ou `↓` | Baixo |
| `A` ou `←` | Esquerda |
| `D` ou `→` | Direita |
| `ESC` | Sair |

## Funcionalidades

- **Cabeça animada** — olhinhos que apontam para a direção do movimento
- **Cauda com gradiente** — verde escuro na ponta, verde vivo perto da cabeça
- **Comida pulsante** — círculo que pulsa com brilho e glow vermelho
- **Grid no fundo** — grade sutil para facilitar a leitura da posição
- **HUD com score e recorde** — placar visível durante o jogo, recorde salvo na sessão
- **Tela de Game Over** — exibe o score e o melhor resultado por 2 segundos antes de reiniciar
- **Velocidade progressiva** — a cobra acelera a cada 3 pontos

## Estrutura do Projeto

- **`main.py`** — loop principal do jogo, lógica de movimento e colisão
- **`cobra.py`** — classes `Food` e `Snake`, funções de renderização (`draw_tail`, `draw_grid`, `draw_hud`)

## Como Executar

Instale o Pygame (requer versão 2.0+):

```bash
pip install pygame
```

Execute o jogo:

```bash
python main.py
```
