import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicialização do módulo e variáveis
pygame.init()
width = 640
height = 480
x_snake = width / 2
y_snake = height / 2
x_food = randint(15, width - 25)
y_food = randint(15, height - 25)
clock = pygame.time.Clock()
point_sound = pygame.mixer.Sound('songs/smw_1-up.wav')
font = pygame.font.SysFont('arial', 30, True, False)
points = 0
dead = False

speed = 5
x_controller = speed
y_controller = 0




# Configuração da tela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo da Cobrinha')


'''
A ideia é limitarmos o tamanho da lista que contém todas as posições da cobra, para que ela não cresça indefinidamente. Para isso,
definimos um valor máximo e excluímos a posição mais antiga da snake_list.
'''

snake_list = []
snake_length = 1


def drawsnake(snake_list):
    for XeY in snake_list:
        # xEy = [x, y] da posição em que a cobra passou
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], 15, 15))


def restart_game():
    global points, snake_length, x_snake, y_snake, x_food, y_food, dead, snake_list, head_list
    points = 0
    snake_length = 1
    x_snake = width / 2
    y_snake = height / 2
    x_food = randint(15, width)
    y_food = randint(15, height)
    dead = False
    snake_list = []
    head_list = []


def game_over():
    while dead:
        screen.fill((255, 255, 255))
        game_over = f'Game Over! Aperte R para reiniciar'
        text_game_over = font.render(game_over, True, (0, 0, 0))
        screen.blit(text_game_over, (50, 200))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart_game()

        pygame.display.update()


while True:
    message = f'Pontos: {points}'
    clock.tick(50)
    screen.fill((0, 0, 0))
    text = font.render(message, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controller == speed:
                    pass
                else:
                    x_controller = -speed
                    y_controller = 0
                

            if event.key == K_d:
                if x_controller == -speed:
                    pass
                else:
                    x_controller = speed
                    y_controller = 0

            if event.key == K_w:
                if y_controller == speed:
                    pass
                else:
                    y_controller = -speed
                    x_controller = 0

            if event.key == K_s:
                if y_controller == -speed:
                    pass
                else:
                    y_controller = speed
                    x_controller = 0

    x_snake += x_controller
    y_snake += y_controller

    # Cobrinha
    snake = pygame.draw.rect(screen, (0, 255, 0), (x_snake, y_snake, 15, 15))

    # Comida
    food = pygame.draw.rect(screen, (255, 0, 0), (x_food, y_food, 15, 15))


    # Colisão
    if snake.colliderect(food):
        x_food = randint(10, width)
        y_food = randint(10, height)
        point_sound.play()
        points += 1
        snake_length += 5
    


    # Lista que guarda a posição mais recente (x, y) da cabeça da cobra
    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)


    # Morte nos limites da tela
    if head_list[0] == width:
        dead = True
        game_over()
        continue

    if head_list[0] == 0:
        dead = True
        game_over()
        continue

    if head_list[1] == height:
        dead = True
        game_over()
        continue

    if head_list[1] == 0:
        dead = True
        game_over()
        continue


    # Lista que guarda todas as posições passadas pela cobra
    snake_list.append(head_list)


    # Se tiver mais de uma lista igual a lista cabeça dentro da lista da cobra, ela se encostou, logo perdeu.
    if snake_list.count(head_list) > 1:
        dead = True
        game_over()


    # Essa condição deleta a posição mais antiga da cabeça da cobra
    if len(snake_list) > snake_length:
        del snake_list[0]
    

    # Posiciona o texto na tela
    screen.blit(text, (450, 40))

    drawsnake(snake_list)

    # Atualiza a tela
    pygame.display.update()


