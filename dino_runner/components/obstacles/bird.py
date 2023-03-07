import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird (Obstacle):
    def __init__ (self, bird_height,image):
        self.type = random.randint(0, 2)
        super().__init__(self.type,image)
        if bird_height == 0:
            self.rect.y = 150
        elif bird_height == 1:
            self.rect.y = 250
        elif bird_height == 2:
            self.rect.y = 320
