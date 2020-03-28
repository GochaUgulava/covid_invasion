import pygame
import random
from pygame.sprite import Sprite

import game_functions as gf


class CellAll(Sprite):
    def __init__(self, game_set, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_set = game_set
        self.get_image_name()
        self.image_orig = pygame.image.load(gf.get_path(self.image_name))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, self.screen_rect.right - 80)
        self.rect.y = random.randrange(-110, -100)
        self.rot = 0
        self.rot_speed = random.choice([-5, -3, 3, 5])
        self.last_update = pygame.time.get_ticks()
        self.explosion_anim = []
        self.load_explosion_anim_images()

    def get_image_name(self):
        self.image_name = "NotImplementedError"
        raise NotImplementedError

    def update(self):
        self.rect.centery += self.game_set.cell_speed_factor
        self.rotate()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def load_explosion_anim_images(self):
        raise NotImplementedError


class Cell(CellAll):
    def get_image_name(self):
        self.image_name = random.choice(["red.bmp", "white.bmp", "mono.bmp"])

    def load_explosion_anim_images(self):
        if self.image_name == "red.bmp":
            file_prefix = "red"
        elif self.image_name == "white.bmp":
            file_prefix = "white"
        else:
            file_prefix = "mono"
        for i in range(1, 7):
            filename = file_prefix + '{}.bmp'.format(i)
            img = pygame.image.load(gf.get_path(filename))
            self.explosion_anim.append(img)


class Covid(CellAll):
    def get_image_name(self):
        self.image_name = "covid.bmp"

    def load_explosion_anim_images(self):
        for i in range(1, 7):
            filename = 'covid{}.bmp'.format(i)
            img = pygame.image.load(gf.get_path(filename))
            self.explosion_anim.append(img)
