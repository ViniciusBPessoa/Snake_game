import pygame
import Cobra_pulsante
from random import choice

pygame.init()

size_game = 30
tabel_size = 20
tale_size = 2
color = (0, 255, 0)
fps = 12
direção = "baixo"


size_display_x = tabel_size * size_game
size_display_y = tabel_size * size_game
pints = [x for x in range (0, (size_game * tabel_size) + 1) if x % size_game == 0 and x != size_game * tabel_size or x == 0]

screan = pygame.display.set_mode((size_display_x, size_display_y))
pygame.display.set_caption("Cobrita")

food = Cobra_pulsante.Food(size = size_game, posi_x = choice(pints), posi_y = choice(pints))
cobrita = Cobra_pulsante.sanke(size = size_game, posi_x = choice(pints), posi_y = choice(pints), color = color)
tiks = pygame.time.Clock()

efeito_acerto = pygame.mixer.Sound('musica/acerto.wav')
efeito_erro = pygame.mixer.Sound('musica/erro.wav')

tale_snake = []
is_presing = False

while True:
    
    tiks.tick(fps)
    screan.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN and is_presing == False:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            
            if event.key == pygame.K_d:
                if direção != "esquerda":
                    direção = "direita"
            
            if event.key == pygame.K_a:
                if direção != "direita":
                    direção = "esquerda"
            
            if event.key == pygame.K_w:
                if direção != "baixo":
                    direção = "cima"
            
            if event.key == pygame.K_s:
                if direção != "cima":
                    direção = "baixo"
        


    if direção == "baixo":
        cobrita.posi_x += 0
        cobrita.posi_y += size_game
    
    if direção == "cima":
        cobrita.posi_x += 0
        cobrita.posi_y -= size_game

    if direção == "esquerda":
        cobrita.posi_x -= size_game
        cobrita.posi_y -= 0
    
    if direção == "direita":
        cobrita.posi_x += size_game
        cobrita.posi_y -= 0

    food.drow_food(screan)
    cobrita.drow_snake(screan)

    if len(tale_snake) > tale_size:
        tale_snake.remove(tale_snake[0])

    if cobrita.posi_x == food.posi_x and cobrita.posi_y == food.posi_y:

        efeito_acerto.play()
        tale_size += 1
        food.randomizer(pints, tale_snake, cobrita.posi_x, cobrita.posi_y)
    
    if cobrita.posi_x < 0 or cobrita.posi_x > size_display_x - size_game or cobrita.posi_y < 0 or cobrita.posi_y > size_display_y - size_game  or (cobrita.posi_x, cobrita.posi_y) in tale_snake:
        efeito_erro.play()
        tale_size = 2
        direção = "baixo"
        tale_snake = []
        cobrita.randomizer(pints)
        food.randomizer(pints, tale_snake, cobrita.posi_x, cobrita.posi_y)

    
    Cobra_pulsante.drow_tale(screan, tale_snake, size_game)
    
    tale_snake.append((cobrita.posi_x, cobrita.posi_y))
    pygame.draw.rect(screan, (255,0,0), (0, 0, size_display_x, size_display_x), 2)
    pygame.display.update()
