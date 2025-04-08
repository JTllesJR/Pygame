import pygame
from pygame.locals import *
from random import randrange
import os

pygame.init()

width_cactus = 32
height_cactus = 32
width_screen = 640
height_screen = 480

main_diretory = 'c:\\Users\\jotel\\OneDrive\\Documentos\\Python\\Pygame\\jogo_dino'
objects_diretory = os.path.join(main_diretory, 'objects')
songs_diretory = os.path.join(main_diretory, 'songs')
img_diretory = os.path.join(main_diretory, 'sprites')

# Importamos a SpriteSheet. O método convert_alpha() mantém a transparência do PNG.
sprite_sheet = pygame.image.load(os.path.join(img_diretory, 'dinoSpritesheet.png'))


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((160, 0), (width_cactus, height_cactus))
        self.image = pygame.transform.scale(self.image, (width_cactus * 2, height_cactus * 2))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (500, 416)
        self.speed = 10

    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.topright[0] < 0:
            self.rect.x = width_screen + randrange(0, 400)