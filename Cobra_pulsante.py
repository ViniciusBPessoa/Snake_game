import pygame
from random import choice

class Food:
    def __init__(self, posi_x = 0, posi_y = 0, size = 10):

        self.posi_x = posi_x
        self.posi_y = posi_y
        self.size = size

    def drow_food(self, scream):

        pygame.draw.rect(scream, (255, 0, 0), (self.posi_x, self.posi_y, self.size, self.size))
        pygame.draw.rect(scream, (0, 0, 0), (self.posi_x, self.posi_y, self.size, self.size), 2)
    
    def randomizer(self, point, tale, hart_x, hart_y):

        while True:

            self.posi_x = choice(point)
            self.posi_y = choice(point)

            if (self.posi_x, self.posi_y) in tale or (self.posi_x, self.posi_y) == (hart_x, hart_y):
                continue
                
            else:
                break

class sanke:

    def __init__(self, posi_x = 0, posi_y = 0, size = 10, color = 0):

        self.posi_x = posi_x
        self.posi_y = posi_y
        self.size = size
        self.color = color
        
    def drow_snake(self, scream):

        pygame.draw.rect(scream, self.color, (self.posi_x, self.posi_y, self.size, self.size))
        pygame.draw.rect(scream, (0, 0, 0), (self.posi_x, self.posi_y, self.size, self.size), 2)
    
    def randomizer(self, point):

        self.posi_x = choice(point)
        self.posi_y = choice(point)

def drow_tale(scream, tale_s, size):

    if len(tale_s) != 0:
        tamanho = len(tale_s)
        variavel = round((255 / tamanho))
        votano = 0
        ino = 255
        vai= True

        for c in tale_s:

            if votano > 255:
                votano = 255
            if ino < 0:

                ino = 255

            pygame.draw.rect(scream, (0, votano, ino), (c[0], c[1], size, size))
            pygame.draw.rect(scream, (0 , 0, 0), (c[0], c[1], size, size), 2)

            if vai:
                votano += variavel * 2

                if votano > 255:

                    vai = False

            else:
                ino -= variavel * 2
