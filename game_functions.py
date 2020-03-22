import sys
import pygame
import os

from cell import Cell


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


def cell_create(game_set, screen, cells):
    """ cell creation in game, avoiding their collision on creation;
         cells are creating  by one in negative y corridor (see Cell class initialization).
    """
    cell_create_flag = True
    cell = Cell(game_set, screen)
    for old_cell in cells.sprites():
        if old_cell.rect.y < 0:
            cell_create_flag = False
            break
    if not pygame.sprite.spritecollideany(cell, cells) and cell_create_flag:
        cells.add(cell)


def cell_update(screen, cells):
    cells.update()
    for cell in cells.sprites():
        if cell.rect.top > screen.get_rect().bottom:
            cells.remove(cell)


def render(game_set, screen, pill, cells):
    screen.fill(game_set.screen_background_color)
    pill.blitme()
    cells.draw(screen)
    pygame.display.flip()
