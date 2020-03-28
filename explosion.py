import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    def __init__(self, explosion_anim, center, screen):
        super().__init__()
        self.screen = screen
        self.explosion_anim = explosion_anim
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 80

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
