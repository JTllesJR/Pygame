import pygame
from pygame.locals import *
from random import randrange
import os

width_bird = 32
height_bird = 32
width_screen = 640


main_diretory = 'c:\\Users\\jotel\\OneDrive\\Documentos\\Python\\Pygame\\jogo_dino'
objects_diretory = os.path.join(main_diretory, 'objects')
songs_diretory = os.path.join(main_diretory, 'songs')
img_diretory = os.path.join(main_diretory, 'sprites')

# Importamos a SpriteSheet. O método convert_alpha() mantém a transparência do PNG.
sprite_sheet = pygame.image.load(os.path.join(img_diretory, 'dinoSpritesheet.png'))

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.index_list = 0
        
        self.bird_images = []
        for c in range(2):
            self.bird_images.append(sprite_sheet.subsurface((width_bird * 3, 0), (width_bird, height_bird)))
            self.bird_images.append(sprite_sheet.subsurface((width_bird * 4, 0), (width_bird, height_bird)))
        
        self.image = self.bird_images[self.index_list]
        self.image = pygame.transform.scale(self.image, (width_bird * 2.5, height_bird * 2.5))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 290)    
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 15


    def update(self):
        self.rect.x -= self.speed

        if self.index_list >= 1:
            self.index_list = 0
        self.index_list += 0.15


        self.image = self.bird_images[int(self.index_list)]
        self.image = pygame.transform.scale(self.image, (width_bird * 2.5, height_bird * 2.5))

        if self.rect.topright[0] < 0:
            self.rect.x = (width_screen + 500) + randrange(0, 1500)


