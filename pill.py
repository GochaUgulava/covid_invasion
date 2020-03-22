import pygame
from pygame.sprite import Sprite

import game_functions as gf


class Pill(Sprite):
    def __init__(self, game_set, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_set = game_set
        self.image = pygame.image.load(gf.get_path("pill.bmp"))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        self.moving_right_flag = False
        self.moving_left_flag = False
        self.moving_up_flag = False
        self.moving_down_flag = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right_flag and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.game_set.pill_speed_factor
        if self.moving_left_flag and self.rect.left > 0:
            self.rect.centerx -= self.game_set.pill_speed_factor
        if self.moving_up_flag and self.rect.top > 0:
            self.rect.centery -= self.game_set.pill_speed_factor
        if self.moving_down_flag and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.game_set.pill_speed_factor
