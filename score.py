import pygame.font
from pygame.sprite import Group

from pill import Pill


class Score:
    def __init__(self, game_set, screen):
        self.game_set = game_set
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (0, 255, 0)
        self.game_active = False
        self.high_score = game_set.high_score
        self.reset_stat()
        self.reset_killed_cell_limit()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_killed_cell()
        self.prep_lifes()

    def reset_stat(self):
        self.level = 1
        self.score = 0
        self.lifes_left = self.game_set.lifes_limit

    def reset_killed_cell_limit(self):
        self.killed_cell_limit = self.game_set.killed_cell_limit

    def prep_score(self):
        score_txt = "{:,}".format(self.score)
        self.score_image = self.font.render(score_txt, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen.get_rect().right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_txt = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_txt, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen.get_rect().right - 20
        self.high_score_rect.top = self.score_rect.bottom + 10

    def prep_level(self):
        level_txt = str(self.level)
        self.level_image = self.font.render(level_txt, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen.get_rect().right - 20
        self.level_rect.top = self.high_score_rect.bottom + 10

    def prep_killed_cell(self):
        killed_cell_limit_txt = str(self.killed_cell_limit)
        self.killed_cell_limit_image = self.font.render(killed_cell_limit_txt, True, self.text_color)
        self.killed_cell_limit_rect = self.killed_cell_limit_image.get_rect()
        self.killed_cell_limit_rect.left = self.screen.get_rect().left + 10
        self.killed_cell_limit_rect.top = 20

    def prep_lifes(self):
        self.lifes = Group()
        for pill_number in range(self.lifes_left):
            pill = Pill(self.game_set, self.screen)
            pill.rect.x = self.killed_cell_limit_rect.right + 10 + pill_number * pill.rect.width
            pill.rect.y = 10
            self.lifes.add(pill)

    def show_stat(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.killed_cell_limit_image, self.killed_cell_limit_rect)
        self.lifes.draw(self.screen)
