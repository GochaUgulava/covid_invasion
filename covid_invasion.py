# Voice by Kenney (www.kenney.nl)
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from pill import Pill
from score import Score
from menu import Menu
from sound import Sound


def main():
    game_set = Settings()
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    pygame.display.set_caption("Covid Invasion")
    gf.set_icon()
    clock = pygame.time.Clock()
    score = Score(game_set, screen)
    pill = Pill(game_set, screen)
    cells = Group()
    covids = Group()
    pygame.mixer.init()
    sound = Sound(game_set)
    pygame.mixer.music.play(loops=-1)
    menu = Menu(screen)
    while True:
        clock.tick(game_set.fps)
        gf.check_event(pill, menu, score,  cells, covids, sound)
        if score.game_active:
            gf.cell_create(game_set, screen, covids, cells)
            gf.covid_create(game_set, screen, covids, cells)
            gf.cell_update(screen, cells,  covids, pill, score, sound)
            gf.covid_update(game_set, screen, covids, cells, pill, score, sound)
            pill.update()
        gf.render(game_set, screen, pill, covids, cells, score, menu)


main()
