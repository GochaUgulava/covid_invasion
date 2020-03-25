import game_functions as gf


class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.fps = 30
        self.screen_background_color = (255, 0, 100)
        self.pill_speed_factor = 4
        self.cell_speed_factor = 2
        self.cell_number_adjust = 0
        self.covid_number_adjust = 150
        self.lifes_limit = 3
        self.covid_kill_points = 50
        self.killed_cell_limit = 3
        self.music_volume = 0.4
        self.sound_volume = 0.4
        self.high_score = int(self.get_high_score())

    def get_high_score(self):
        try:
            with open(gf.get_path("high_score.txt"), 'r') as file:
                try:
                    return file.read().rstrip()
                except ValueError:
                    return 0
        except FileNotFoundError:
            return 0
