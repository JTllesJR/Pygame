import pygame
from pygame.locals import *
from objects.dino import sprite_sheet
import os

width_floor = 32
height_floor = 32
width_screen = 640
height_screen = 480

main_diretory = 'c:\\Users\\jotel\\OneDrive\\Documentos\\Python\\Pygame\\jogo_dino'
objects_diretory = os.path.join(main_diretory, 'objects')
songs_diretory = os.path.join(main_diretory, 'songs')
img_diretory = os.path.join(main_diretory, 'sprites')

# Importamos a SpriteSheet. O método convert_alpha() mantém a transparência do PNG.
sprite_sheet = pygame.image.load(os.path.join(img_diretory, 'dinoSpritesheet.png'))


class Floor(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((192, 0), (width_floor, height_floor))
        self.image = pygame.transform.scale(self.image, (width_floor * 2, height_floor * 2))
        self.rect = self.image.get_rect()
        self.rect.y = height_screen - 64
        self.rect.x = pos_x * 64
        self.speed = 10



    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = width_screen
            self.rect.y = height_screen - 64
        self.rect.x -= self.speed