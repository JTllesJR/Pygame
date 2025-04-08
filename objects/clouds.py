import pygame
from pygame.locals import *
from random import randrange
import os

width_cloud = 32
height_cloud = 32
width_screen = 640

main_diretory = 'c:\\Users\\jotel\\OneDrive\\Documentos\\Python\\Pygame\\jogo_dino'
objects_diretory = os.path.join(main_diretory, 'objects')
songs_diretory = os.path.join(main_diretory, 'songs')
img_diretory = os.path.join(main_diretory, 'sprites')

# Importamos a SpriteSheet. O método convert_alpha() mantém a transparência do PNG.
sprite_sheet = pygame.image.load(os.path.join(img_diretory, 'dinoSpritesheet.png'))

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = (sprite_sheet.subsurface((224, 0), (32, 32)))
        self.image = self.img
        self.image = pygame.transform.scale(self.image, (width_cloud * 3, height_cloud * 3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.speed = 10

        
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = randrange(width_screen, width_screen + 300, 90)
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= self.speed

    

