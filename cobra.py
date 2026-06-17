import pygame
from random import choice
import math


class Food:
    def __init__(self, posi_x=0, posi_y=0, size=10):
        self.posi_x = posi_x
        self.posi_y = posi_y
        self.size = size

    def draw(self, screen, tick):
        cx = self.posi_x + self.size // 2
        cy = self.posi_y + self.size // 2
        pulse = (math.sin(tick * 0.15) + 1) / 2
        r = int(self.size // 2 * (0.75 + 0.25 * pulse))

        glow = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 40, 40, 50), (self.size * 2, self.size * 2), r + 6)
        screen.blit(glow, (cx - self.size * 2, cy - self.size * 2))

        pygame.draw.circle(screen, (220, 30, 30), (cx, cy), r)
        pygame.draw.circle(screen, (255, 140, 140), (cx - r // 3, cy - r // 3), max(1, r // 3))

    def randomize(self, points, tail, head_x, head_y):
        while True:
            self.posi_x = choice(points)
            self.posi_y = choice(points)
            if (self.posi_x, self.posi_y) not in tail and (self.posi_x, self.posi_y) != (head_x, head_y):
                break


class Snake:
    def __init__(self, posi_x=0, posi_y=0, size=10, color=(0, 200, 0)):
        self.posi_x = posi_x
        self.posi_y = posi_y
        self.size = size
        self.color = color

    def draw_head(self, screen, direction):
        s = self.size
        x, y = self.posi_x, self.posi_y

        pygame.draw.rect(screen, (25, 160, 25), (x, y, s, s), border_radius=4)
        pygame.draw.rect(screen, (60, 220, 60), (x + 1, y + 1, s - 2, s - 2), border_radius=3)

        e = max(2, s // 5)
        if direction == "direita":
            e1, e2 = (x + s - e - 2, y + 2), (x + s - e - 2, y + s - e - 2)
        elif direction == "esquerda":
            e1, e2 = (x + 2, y + 2), (x + 2, y + s - e - 2)
        elif direction == "cima":
            e1, e2 = (x + 2, y + 2), (x + s - e - 2, y + 2)
        else:
            e1, e2 = (x + 2, y + s - e - 2), (x + s - e - 2, y + s - e - 2)

        pygame.draw.rect(screen, (0, 0, 0), (*e1, e, e))
        pygame.draw.rect(screen, (0, 0, 0), (*e2, e, e))
        pygame.draw.rect(screen, (255, 255, 255), (e1[0] + 1, e1[1], 1, 1))
        pygame.draw.rect(screen, (255, 255, 255), (e2[0] + 1, e2[1], 1, 1))

    def randomize(self, points):
        self.posi_x = choice(points)
        self.posi_y = choice(points)


def draw_tail(screen, tail, size):
    total = len(tail)
    if not total:
        return
    for i, (tx, ty) in enumerate(tail):
        t = i / max(1, total - 1)
        r = int(10 + t * 15)
        g = int(70 + t * 160)
        b = int(30 + t * 10)
        pygame.draw.rect(screen, (r, g, b), (tx + 1, ty + 1, size - 2, size - 2), border_radius=3)


def draw_grid(screen, cell, width, height):
    for x in range(0, width + 1, cell):
        pygame.draw.line(screen, (18, 18, 18), (x, 0), (x, height))
    for y in range(0, height + 1, cell):
        pygame.draw.line(screen, (18, 18, 18), (0, y), (width, y))


def draw_hud(screen, score, high_score, font):
    s_surf = font.render(f"Score: {score}", True, (170, 170, 170))
    h_surf = font.render(f"Best:  {high_score}", True, (255, 210, 0))
    screen.blit(s_surf, (8, 8))
    screen.blit(h_surf, (8, 30))
