import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from pill import Pill


def main():
    game_set = Settings()
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    pygame.display.set_caption("Covid Invasion")
    gf.set_icon()
    clock = pygame.time.Clock()
    pill = Pill(game_set, screen)
    cells = Group()
    covids = Group()
    while True:
        clock.tick(game_set.fps)
        gf.check_event(pill)
        gf.cell_create(game_set, screen, covids, cells)
        gf.covid_create(game_set, screen, covids, cells)
        gf.cell_update(screen, cells)
        gf.covid_update(screen, covids)
        pill.update()
        gf.render(game_set, screen, pill, covids, cells)


main()
