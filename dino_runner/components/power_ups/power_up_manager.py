import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
        self.duration = random.randint(3, 5)


    def generate_power_up(self):
        if self.power_up_type == 1:
           self.when_appears += random.randint(150, 200)
           power_up = Shield()
           self.power_ups.append(power_up)
        elif self.power_up_type == 2:
            self.when_appears += random.randint(150, 200)
            power_up = Hammer()
            self.power_ups.append(power_up)

    def update(self, game):
        self.power_up_type = random.randint(1, 2)
        if len(self.power_ups) == 0 and self.when_appears == game.score:
          self.generate_power_up()


        for power_up in self. power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration *1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint (200 , 300)