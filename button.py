import pygame.font


class Button:
    def __init__(self, screen, msg, order_number):
        self.screen = screen
        self.msg = msg
        self.order_number = order_number
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (255, 255, 255)
        self.button_color = (0, 0, 255)
        self.width, self.height = 250, 70
        self.prep_button()

    def prep_button(self):
        button_y = 150 + self.order_number * 100
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.centery = button_y
        self.button_image = self.font.render(self.msg, True, self.text_color,
                                            self.button_color)
        self.button_rect = self.button_image.get_rect()
        self.button_rect.centerx = self.screen.get_rect().centerx
        self.button_rect.centery = button_y


    def show_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.button_image, self.button_rect)
