import pygame

import game_functions as gf


class Sound:
    def __init__(self, game_set):
        self.game_set = game_set
        self.ready = pygame.mixer.Sound(gf.get_path('ready.wav'))
        self.go = pygame.mixer.Sound(gf.get_path('go.wav'))
        self.wrong = pygame.mixer.Sound(gf.get_path('wrong.wav'))
        self.correct = pygame.mixer.Sound(gf.get_path('correct.wav'))
        self.level_up = pygame.mixer.Sound(gf.get_path('level_up.wav'))
        self.mission_failed = pygame.mixer.Sound(gf.get_path('mission_failed.wav'))
        self.game_over = pygame.mixer.Sound(gf.get_path('game_over.wav'))
        pygame.mixer.music.load(gf.get_path('maintheme.wav'))
        pygame.mixer.music.set_volume(game_set.music_volume)

    def play(self, voice):
        voice.set_volume(self.game_set.sound_volume)
        voice.play()
