import sys
import pygame
import os
from time import sleep

from cell import Cell, Covid


def check_event(pill, menu, score,  cells, covids, sound):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, pill, score, cells, covids, sound)
        elif event.type == pygame.KEYUP:
            check_key_up(event, pill)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button(menu, score, cells, covids, mouse_x, mouse_y, sound)


def check_key_down(event, pill, score, cells, covids, sound):
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
    elif not score.game_active and event.key == pygame.K_RETURN:
        new_game(score, cells, covids, sound)


def check_key_up(event, pill):
    if event.key == pygame.K_RIGHT:
        pill.moving_right_flag = False
    elif event.key == pygame.K_LEFT:
        pill.moving_left_flag = False
    elif event.key == pygame.K_UP:
        pill.moving_up_flag = False
    elif event.key == pygame.K_DOWN:
        pill.moving_down_flag = False


def check_button(menu, score, cells, covids, mouse_x, mouse_y, sound):
    if menu.button_play.rect.collidepoint(mouse_x, mouse_y) and not score.game_active:
        new_game(score, cells, covids, sound)
    elif menu.button_instructions.rect.collidepoint(mouse_x, mouse_y) and not score.game_active:
        show_instructions()
    elif menu.button_quit.rect.collidepoint(mouse_x, mouse_y) and not score.game_active:
        sys.exit()


def get_path(file_name):
    game_folder = os.path.dirname(__file__)
    data_folder = os.path.join(game_folder, "data")
    file_path = os.path.join(data_folder, file_name)
    return file_path


def set_icon():
    icon_image = pygame.image.load(get_path("warning.ico"))
    pygame.display.set_icon(icon_image)


def new_game(score, cells, covids, sound):
    score.game_active = True
    pygame.mouse.set_visible(False)
    score.reset_stat()
    score.reset_killed_cell_limit()
    score.prep_score()
    score.prep_high_score()
    score.prep_level()
    score.prep_killed_cell()
    score.prep_lifes()
    cells.empty()
    covids.empty()
    sound.play(sound.ready)
    sleep(1)
    sound.play(sound.go)


def show_instructions():
    pass


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


def cell_update(screen, cells,  covids, pill, score, sound):
    cells.update()
    for cell in cells.sprites():
        if cell.rect.top > screen.get_rect().bottom:
            cells.remove(cell)
    check_pill_cell_collision(cells, covids, pill, score, sound)


def check_pill_cell_collision(cells, covids, pill, score, sound):
    if pygame.sprite.spritecollide(pill, cells, True):
        sound.play(sound.wrong)
        if score.killed_cell_limit > 1:
            score.killed_cell_limit -= 1
            score.prep_killed_cell()
        else:
            pill_collided(score, covids, cells, sound)



def covid_update(game_set, screen, covids, cells, pill, score, sound):
    covids.update()
    for covid in covids.sprites():
        if covid.rect.top > screen.get_rect().bottom:
            covid.remove(covids)
            pill_collided(score, covids, cells, sound)
    check_pill_covid_collision(game_set, covids, pill, score, sound)


def check_pill_covid_collision(game_set, covids, pill, score, sound):
    if pygame.sprite.spritecollide(pill, covids, True):
        sound.play(sound.correct)
        score.score += game_set.covid_kill_points
        if score.score % 500 == 0 and score.score != 0:
            increase_level(game_set, score, sound)
        score.prep_score()
        check_high_score(score)


def increase_level(game_set, score, sound):
    sleep(1)
    sound.play(sound.level_up)
    game_set.fps += 5
    score.level += 1
    score.prep_level()


def check_high_score(score):
    if score.score > score.high_score:
        score.high_score = score.score
        score.prep_high_score()


def pill_collided(score, covids, cells, sound):
    if score.lifes_left > 1:
        score.lifes_left -= 1
        score.prep_lifes()
        score.reset_killed_cell_limit()
        score.prep_killed_cell()
        covids.empty()
        cells.empty()
        sleep(1)
        sound.play(sound.mission_failed)
    else:
        game_over(score, sound)


def game_over(score, sound):
    sleep(1)
    sound.play(sound.game_over)
    score.game_active = False
    pygame.mouse.set_visible(True)


def render(game_set, screen, pill, covids, cells, score, menu):
    screen.fill(game_set.screen_background_color)
    pill.blitme()
    cells.draw(screen)
    covids.draw(screen)
    score.show_stat()
    if not score.game_active:
        menu.show_menu()
    pygame.display.flip()
