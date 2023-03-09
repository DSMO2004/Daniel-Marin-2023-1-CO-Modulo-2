import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.power_ups.projectile import Projectile

from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT


class ObstacleManager:
  def __init__(self):
    self.obstacles = []
    self.projectile = Projectile()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  def generate_obstacle(self, obstacle_type):
    if obstacle_type == 0:
      cactus_type = 'SMALL'
      obstacle = Cactus(cactus_type)
    elif obstacle_type == 1:
      cactus_type = 'LARGE'
      obstacle = Cactus(cactus_type)
    else:
      obstacle = Bird()
    return obstacle

  def update(self, game):
    if len(self.obstacles) == 0:
      obstacle_type = random.randint(0, 2)
      obstacle = self.generate_obstacle(obstacle_type)
      self.obstacles.append(obstacle)

    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)

      if game.player.dino_rect.colliderect(obstacle.rect):
        if game.player.type != SHIELD_TYPE and HAMMER_TYPE:
           pygame.time.delay(1000)
           game.death_count +=1
           game.playing = False
           break
        else:
          self.obstacles.remove(obstacle)
        
      if game.player.type == HAMMER_TYPE:
           self.projectile
           self.projectile.draw(self.screen)
           if game.projectile_rect.colliderect(obstacle.rect):
             self.obstacles.remove(obstacle)



  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)

  def reset_obstacles(self):
    self.obstacles = []