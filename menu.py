import pygame

from button import Button
import game_functions as gf


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.prep_menu_image()
        self.prep_menu()

    def prep_menu_image(self):
        self.menu_image = pygame.image.load(gf.get_path("covinv.bmp"))
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.centerx = self.screen.get_rect().centerx
        self.menu_rect.centery = 100


    def prep_menu(self):
        self.button_play = Button(self.screen, "Play", 250)
        self.button_instructions = Button(self.screen, "Instructions", 320)
        self.button_settings = Button(self.screen, "Settings", 390)
        self.button_quit = Button(self.screen, "Quit", 460)

    def show_menu(self):
        self.screen.blit(self.menu_image, self.menu_rect)
        self.button_play.show_button()
        self.button_instructions.show_button()
        self.button_settings.show_button()
        self.button_quit.show_button()
