import pygame
import sys


from slidebar import SlideBar
from button import Button


def set_settings(screen, game_set, sound):
    pygame.mouse.set_visible(True)
    mouse_drag_flag = False
    text_image, text_rect = prep_page_title()
    slider_music = SlideBar(screen, "MUSIC", 300, 150, 0, 1, game_set.music_volume)
    slider_sound = SlideBar(screen, "SOUND", 300, 220, 0, 1, game_set.sound_volume)
    slider_fps = SlideBar(screen, "GAME SPEED", 300, 290, 20, 80, game_set.fps)
    slider_covid = SlideBar(screen, "COVIDS", 300, 360, 0, 300, game_set.covid_number_adjust)
    button_ok = Button(screen, "OK", 500)
    slider_which = slider_music
    #  need to send information into the set_value function
    slider_name = "music"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if slider_music.rect_indicator.collidepoint(mouse_x, mouse_y):
                    slider_which = slider_music
                    slider_name = "music"
                    mouse_drag_flag = True
                if slider_sound.rect_indicator.collidepoint(mouse_x, mouse_y):
                    slider_which = slider_sound
                    slider_name = "sound"
                    mouse_drag_flag = True
                if slider_fps.rect_indicator.collidepoint(mouse_x, mouse_y):
                    slider_which = slider_fps
                    slider_name = "fps"
                    mouse_drag_flag = True
                if slider_covid.rect_indicator.collidepoint(mouse_x, mouse_y):
                    slider_which = slider_covid
                    slider_name = "covid"
                    mouse_drag_flag = True
                if button_ok.rect.collidepoint(mouse_x, mouse_y):
                    return
            elif event.type == pygame.MOUSEBUTTONUP:
                if mouse_drag_flag:
                    mouse_drag_flag = False
                    set_value(game_set, sound, slider_which, slider_name)
            elif event.type == pygame.MOUSEMOTION:
                if mouse_drag_flag:
                    slider_which.check_indicator(pygame.mouse.get_pos()[0])
        screen.fill((255, 0, 100))
        screen.blit(text_image, text_rect)
        slider_music.show_slider()
        slider_sound.show_slider()
        slider_fps.show_slider()
        slider_covid.show_slider()
        button_ok.show_button()
        pygame.display.flip()


def prep_page_title():
    font = pygame.font.SysFont(None, 48)
    text_image = font.render("Settings", True, (0, 255, 0))
    text_rect = text_image.get_rect()
    text_rect.centerx = 300
    text_rect.centery = 50
    return text_image, text_rect


def set_value(game_set, sound, slider_which, slider_name):
    if slider_name == "music":
        pygame.mixer.music.stop()
        game_set.music_volume = round(slider_which.get_setting_value(), 1)
        sound.music_volume(game_set)
        pygame.mixer.music.play(loops=-1)
    if slider_name == "sound":
        game_set.sound_volume = round(slider_which.get_setting_value(), 1)
    if slider_name == "fps":
        game_set.fps = int(slider_which.get_setting_value())
        game_set.fps_start = game_set.fps
    if slider_name == "covid":
        game_set.covid_number_adjust = 300 - int(slider_which.get_setting_value())
