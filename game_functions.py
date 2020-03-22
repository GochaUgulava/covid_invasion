import sys
import pygame
import os

from cell import Cell, Covid


def check_event(pill):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, pill)
        elif event.type == pygame.KEYUP:
            check_key_up(event, pill)


def check_key_down(event, pill):
    if event.key == pygame.K_RIGHT:
        pill.moving_right_flag = True
    elif event.key == pygame.K_LEFT:
        pill.moving_left_flag = True
    elif event.key == pygame.K_UP:
        pill.moving_up_flag = True
    elif event.key == pygame.K_DOWN:
        pill.moving_down_flag = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_key_up(event, pill):
    if event.key == pygame.K_RIGHT:
        pill.moving_right_flag = False
    elif event.key == pygame.K_LEFT:
        pill.moving_left_flag = False
    elif event.key == pygame.K_UP:
        pill.moving_up_flag = False
    elif event.key == pygame.K_DOWN:
        pill.moving_down_flag = False


def get_path(file_name):
    game_folder = os.path.dirname(__file__)
    data_folder = os.path.join(game_folder, "data")
    file_path = os.path.join(data_folder, file_name)
    return file_path


def set_icon():
    icon_image = pygame.image.load(get_path("warning.ico"))
    pygame.display.set_icon(icon_image)


def cell_create(game_set, screen, covids, cells):
    """ cell creation in game, avoiding their collision on creation;
         cells are creating  by one in game_set.cell_number_adjust defined corridor.
    """
    cell_create_flag = True
    cell = Cell(game_set, screen)
    for old_cell in cells.sprites():
        if old_cell.rect.y < game_set.cell_number_adjust:
            cell_create_flag = False
            break
    if (not pygame.sprite.spritecollide(cell, cells, 0) and
        not pygame.sprite.spritecollide(cell, covids, 0) and
            cell_create_flag):
        cells.add(cell)


def covid_create(game_set, screen, covids, cells):
    """ covid creation in game;
        similar as in cell_create
    """
    covid_create_flag = True
    covid = Covid(game_set, screen)
    for old_covid in covids.sprites():
        if old_covid.rect.y < game_set.covid_number_adjust:
            covid_create_flag = False
            break
    if (not pygame.sprite.spritecollide(covid, cells, 0) and
        not pygame.sprite.spritecollide(covid, covids, 0) and
            covid_create_flag):
        covids.add(covid)


def cell_update(screen, cells):
    cells.update()
    for cell in cells.sprites():
        if cell.rect.top > screen.get_rect().bottom:
            cells.remove(cell)


def covid_update(screen, covids):
    covids.update()
    for covid in covids.sprites():
        if covid.rect.top > screen.get_rect().bottom:
            covid.remove(covids)
            # game over


def render(game_set, screen, pill, covids, cells):
    screen.fill(game_set.screen_background_color)
    pill.blitme()
    cells.draw(screen)
    covids.draw(screen)
    pygame.display.flip()
