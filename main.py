import pygame
from pygame.locals import *
import os
from objects.dino import Dino
from objects.bird import Bird
from objects.cactus import Cactus
from objects.clouds import Cloud
from objects.floor import Floor
from random import randrange

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('arial', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado


all_clouds = []
speed_game = 10
def aumenta_velocidade():
    for c in range(4):
        all_clouds[c].speed = speed_game + 1
    bird.speed = speed_game + 1
    cactus.speed = speed_game + 1
    floor.speed = speed_game + 5
    


def restart_game():
    global pontos, colidiu
    pontos = 0
    colidiu = False
    bird.rect.x = (width + 500) + randrange(0, 1500)
    cactus.rect.x = width + randrange(0, 400)
    dino.rect.center = (100, 415)
    dino.pulo = False
    


# Guardando o caminho do diretório desse projeto, e dos sons utilizados
main_diretory = 'c:\\Users\\jotel\\OneDrive\\Documentos\\Python\\Pygame\\jogo_dino'
songs_diretory = os.path.join(main_diretory, 'songs')
death_sound = pygame.mixer.Sound(os.path.join(songs_diretory, 'death_sound.wav'))
score_sound = pygame.mixer.Sound(os.path.join(songs_diretory, 'score_sound.wav'))

# Inicialização do módulo e variáveis/constantes
pygame.init()
width = 640
height = 480
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
colidiu = False
pontos = 0

# Configurações da tela
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption("Jogo do Dinossauro")


all_sprites = pygame.sprite.Group()
dino = Dino()
bird = Bird()
cactus = Cactus()
all_sprites.add(dino)


# Criando o chão
for i in range(width//64+8):
    floor = Floor(i)
    all_sprites.add(floor)


# Criando as nuvens
for c in range(4):
    clouds = Cloud()
    all_clouds.append(clouds)
    all_sprites.add(clouds)



# Grupo de obstáculos
obstacle_group = pygame.sprite.Group()
obstacle_group.add(cactus, bird)



while True:
    clock.tick(30)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                dino.jump()

            if event.key == K_DOWN:
                dino.goDown()

            if event.key == K_r and colidiu:
                restart_game()



    # Configurando GAME OVER
    collision = pygame.sprite.spritecollide(dino, obstacle_group, False, pygame.sprite.collide_mask)

    if collision and not colidiu:
        death_sound.play()
        colidiu = True
    
    if colidiu:
        if pontos % 100 == 0:
            pontos += 1
        
        game_over = exibe_mensagem("GAME OVER", 40, black)
        pontuacao = exibe_mensagem(f"Sua pontuação foi: {pontos}", 20, black)
        restart = exibe_mensagem('Pressione r para reiniciar', 20, black)
        screen.blit(game_over, (width // 2, height // 2))
        screen.blit(pontuacao, (width // 2, 295))
        screen.blit(restart, (width // 2, 320))

    else:
        pontos += 1
        all_sprites.draw(screen)
        texto_pontos = exibe_mensagem(pontos, 40, black)
        obstacle_group.draw(screen)
        obstacle_group.update()
        all_sprites.update()
        screen.blit(texto_pontos, (520, 30))
        
        if pontos % 100 == 0:
            score_sound.play()
            aumenta_velocidade()

    pygame.display.flip()
