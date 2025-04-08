import pygame
from pygame.locals import *
import os

pygame.init()
pygame.mixer.init()
width_dino = 32
height_dino = 32
width_screen = 640
height_screen = 480

# Guardando o caminho do diretório desse projeto, e dos sons utilizados
main_diretory = 'c:\\Users\\jotel\\OneDrive\\Documentos\\Python\\Pygame\\jogo_dino'
objects_diretory = os.path.join(main_diretory, 'objects')
songs_diretory = os.path.join(main_diretory, 'songs')
img_diretory = os.path.join(main_diretory, 'sprites')

# Importamos a SpriteSheet. O método convert_alpha() mantém a transparência do PNG.
sprite_sheet = pygame.image.load(os.path.join(img_diretory, 'dinoSpritesheet.png'))


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imgs_dino = []
        for c in range(3):
            img = sprite_sheet.subsurface((c * width_dino, 0), (width_dino, height_dino))
            img = pygame.transform.scale(img, (width_dino * 3, height_dino * 3)) # Aumentando o tamanho do dinossauro
            self.imgs_dino.append(img)

        self.index_list = 0
        self.pos_y_init = 367
        self.image = self.imgs_dino[self.index_list]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 415)
        self.pulo = False
        self.jump_song = pygame.mixer.Sound(os.path.join(songs_diretory, 'jump_sound.wav'))
        self.down = False




    def jump(self):
        self.pulo = True
        self.jump_song.play()


    def goDown(self):
        self.down = True

    def update(self):
        if self.index_list >= 2:
            self.index_list = 0
        self.index_list += 0.25
        self.image = self.imgs_dino[int(self.index_list)]


        if self.pulo:
            if self.rect.y <= 250:
                self.pulo = False
            self.rect.y -= 10
            
        else:
            if self.rect.y < self.pos_y_init:
                self.rect.y += 10
            else:
                self.rect.y == self.pos_y_init
