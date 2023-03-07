import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.bird_heights = ["high", "middle", "low"]
        self.bird_size=BIRD[0]
        self.step_index=0

    def update(self, game):
        
        if len(self.obstacles) == 0:
            obstacle_type = random.choice(["cactus", "bird"])

            if obstacle_type == "cactus":
                 cactus_size = random.choice([SMALL_CACTUS, LARGE_CACTUS])

                 if cactus_size == LARGE_CACTUS:
                    cactus = Cactus(cactus_size, y=300)
                 else:
                  cactus = Cactus(cactus_size)

                 self.obstacles.append(cactus)
            else:
                if self.bird_size==BIRD[0] and self.step_index<5:
                     bird = Bird(random.choice(self.bird_heights), BIRD[0])
                     self.obstacles.append(bird)
                     self.step_index += 1
                else: 
                    bird = Bird(random.choice(self.bird_heights),BIRD[1])
                    self.obstacles.append(bird)
                    self.step_index += 1
                if self.step_index >= 10:
                  self.step_index = 0
           

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing= False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)