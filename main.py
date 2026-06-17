import pygame
import cobra
from random import choice

pygame.init()

CELL = 20
COLS = 40
WIN_W = CELL * COLS
WIN_H = CELL * COLS
FPS_BASE = 10
TAIL_START = 5

screen = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Cobrita")

font = pygame.font.SysFont("monospace", 18, bold=True)
big_font = pygame.font.SysFont("monospace", 52, bold=True)
mid_font = pygame.font.SysFont("monospace", 22, bold=True)

points = list(range(0, WIN_W, CELL))

snake = cobra.Snake(size=CELL, posi_x=choice(points), posi_y=choice(points))
food = cobra.Food(size=CELL, posi_x=choice(points), posi_y=choice(points))

clock = pygame.time.Clock()
tick = 0
tail = []
direction = "baixo"
score = 0
high_score = 0
fps = FPS_BASE
game_over_until = 0
last_score = 0


def reset():
    global tail, direction, score, fps
    tail = []
    direction = "baixo"
    score = 0
    fps = FPS_BASE
    snake.randomize(points)
    food.randomize(points, tail, snake.posi_x, snake.posi_y)


while True:
    tick += 1
    now = pygame.time.get_ticks()

    if now < game_over_until:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        screen.fill((20, 0, 0))
        msg = big_font.render("GAME OVER", True, (255, 50, 50))
        sub = mid_font.render(f"Score: {last_score}    Best: {high_score}", True, (200, 200, 200))
        tip = font.render("reiniciando...", True, (80, 80, 80))
        screen.blit(msg, (WIN_W // 2 - msg.get_width() // 2, WIN_H // 2 - 70))
        screen.blit(sub, (WIN_W // 2 - sub.get_width() // 2, WIN_H // 2 + 10))
        screen.blit(tip, (WIN_W // 2 - tip.get_width() // 2, WIN_H // 2 + 50))
        pygame.display.update()
        continue

    clock.tick(fps)
    screen.fill((12, 12, 12))
    cobra.draw_grid(screen, CELL, WIN_W, WIN_H)

    pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if not pressed:
                if event.key in (pygame.K_d, pygame.K_RIGHT) and direction != "esquerda":
                    direction = "direita"
                    pressed = True
                elif event.key in (pygame.K_a, pygame.K_LEFT) and direction != "direita":
                    direction = "esquerda"
                    pressed = True
                elif event.key in (pygame.K_w, pygame.K_UP) and direction != "baixo":
                    direction = "cima"
                    pressed = True
                elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != "cima":
                    direction = "baixo"
                    pressed = True

    if direction == "baixo":      snake.posi_y += CELL
    elif direction == "cima":     snake.posi_y -= CELL
    elif direction == "esquerda": snake.posi_x -= CELL
    elif direction == "direita":  snake.posi_x += CELL

    if (snake.posi_x < 0 or snake.posi_x >= WIN_W or
            snake.posi_y < 0 or snake.posi_y >= WIN_H or
            (snake.posi_x, snake.posi_y) in tail):
        last_score = score
        if score > high_score:
            high_score = score
        game_over_until = pygame.time.get_ticks() + 2000
        reset()
        continue

    if snake.posi_x == food.posi_x and snake.posi_y == food.posi_y:
        score += 1
        fps = FPS_BASE + score // 3
        food.randomize(points, tail, snake.posi_x, snake.posi_y)

    if len(tail) >= TAIL_START + score:
        tail.pop(0)

    cobra.draw_tail(screen, tail, CELL)
    food.draw(screen, tick)
    snake.draw_head(screen, direction)
    cobra.draw_hud(screen, score, high_score, font)

    pygame.draw.rect(screen, (55, 55, 55), (0, 0, WIN_W, WIN_H), 2)

    tail.append((snake.posi_x, snake.posi_y))
    pygame.display.update()
