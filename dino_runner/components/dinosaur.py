import pygame
import random

from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, HAMMER, SCREEN_HEIGHT, SHIELD


class Dinosaur(Sprite):
    X_POS=80
    Y_POS=310
    JUMP_SPEED=8.5
    DUCK_SPEED=340

    def __init__(self):
      self.image = RUNNING [0]
      self.dino_rect = self.image.get_rect()
      self.dino_rect.x = self.X_POS
      self.dino_rect.y = self.Y_POS
      self.step_index = 0
      self.dino_run = True
      self.dino_jump = False
      self.dino_duck = False
      self.jump_speed = self.JUMP_SPEED
      self.duck_speed = self.DUCK_SPEED
      self.hammer_available = False 
      self.hammer_image = HAMMER
      self.hammer_rect = self.hammer_image.get_rect(topleft=(-100, -100))
      self.hammer_speed=25
      self.shile_image=SHIELD
      self.shile_rect=self.shile_image.get_rect(topleft=(-100, -100))
      self.shile_speed=45



    def update(self,user_input):

        if random.random() <= 0.01:
            self.hammer_rect = self.hammer_image.get_rect(topleft=(random.randrange(200,SCREEN_HEIGHT ), random.randint(0, self.dino_rect.y - self.hammer_image.get_height())))
            print(self.hammer_rect.x, self.hammer_rect.y)
            self.hammer_rect.x -= self.hammer_speed
            print( self.hammer_rect.x)

            if self.dino_rect.colliderect(self.hammer_rect):
                self.hammer_available = True

        if random.random() <= 0.005:
            self.shile_rect = self.shile_image.get_rect(topleft=(random.randrange(200,SCREEN_HEIGHT ), random.randint(0, self.dino_rect.y - self.shile_image.get_height())))
            print(self.shile_rect.x, self.shile_rect.y)
            self.shile_rect.x -= self.shile_speed
            print( self.shile_rect.x)

            if self.dino_rect.colliderect(self.shile_rect):
                self.shile_available = True

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck() 

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck= False

        if self.step_index >= 10:
            self.step_index = 0
 

    def run(self):
        self.image = RUNNING[0] if self.step_index<5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
 

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed * 4 
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED :
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED
    

    def duck(self):
        self.image = DUCKING[0] if self.step_index<5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.step_index+=1
        self.dino_rect.y = self.duck_speed
        self.dino_rect.x = self.X_POS +10
        self.dino_duck = False



    

    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))
        screen.blit(self.hammer_image, self.hammer_rect)
        screen.blit(self.image, self.dino_rect)
        screen.blit(self.shile_image,self.shile_rect)





        


 

