import pygame
import pygame.font


class SlideBar:
    def __init__(self, screen, txt, x, y, min_value, max_value, start_value):
        self.screen = screen
        self.x = x
        self.y = y
        self.min_value = min_value
        self.max_value = max_value
        self.start_value = start_value
        self.slider_width = 200
        self.slider_height = 0.05 * self.slider_width
        self.slider_color = (0, 255, 0)
        self.indicator_color = (0, 0, 255)
        self.text_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.txt = txt
        self.scroll_speed = 3
        self.prep_slider()
        self.prep_text()

    def prep_slider(self):
        self.image_line = pygame.Surface((self.slider_width, self.slider_height))
        self.image_line.fill(self.slider_color)
        self.rect_line = self.image_line.get_rect()
        self.rect_line.x = self.x
        self.rect_line.y = self.y
        self.indicator_x  = (self.x + ((self.start_value - self.min_value) / (self.max_value - self.min_value))
                             * self.slider_width)
        self.indicator_y = self.y - (self.slider_height / 2)
        self.image_indicator = pygame.Surface((0.08 * self.slider_width, 2 * self.slider_height))
        self.image_indicator.fill(self.indicator_color)
        self.rect_indicator = self.image_indicator.get_rect()
        self.rect_indicator.x = self.indicator_x
        self.rect_indicator.y = self.indicator_y

    def prep_text(self):
        self.text_image = self.font.render(str(self.txt), True, self.text_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.right = self.x - 20
        self.text_rect.centery = self.rect_indicator.centery

    def show_slider(self):
        self.screen.blit(self.image_line, self.rect_line)
        self.screen.blit(self.image_indicator, self.rect_indicator)
        self.screen.blit(self.text_image, self.text_rect)

    def check_indicator(self, mouse_x):
        if mouse_x > self.rect_indicator.centerx:
            self.update(1)
        if mouse_x == self.rect_indicator.centerx:
            self.update(0)
        if mouse_x < self.rect_indicator.centerx:
            self.update(-1)

    def update(self, flag):
        if self.rect_indicator.x > self.rect_line.x and flag < 0:
            self.rect_indicator.centerx -= self.scroll_speed
        if self.rect_indicator.right < self.rect_line.right and flag > 0:
            self.rect_indicator.centerx += self.scroll_speed

    def get_setting_value(self):
        slider_coefficient = (self.rect_indicator.centerx - self.x)/self.slider_width
        return slider_coefficient * (self.max_value - self.min_value) + self.min_value
