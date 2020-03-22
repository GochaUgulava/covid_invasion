import pygame
import random
from pygame.sprite import Sprite

import game_functions as gf


class Cell(Sprite):
    def __init__(self, game_set, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_set = game_set
        self.image_name = random.choice(["red.bmp", "white.bmp"])
        self.image = pygame.image.load(gf.get_path(self.image_name))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(80, self.screen_rect.right - 80)
        self.rect.y = random.randrange(-110, -100)

    def update(self):
        self.rect.centery += self.game_set.cell_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)
