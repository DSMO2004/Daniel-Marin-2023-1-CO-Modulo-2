import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import HAMMER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import SCREEN_WIDTH

class Projectile(Sprite):
    def __init__(self):
        self.dinosaur= Dinosaur()
        self.image = HAMMER  
        self.rect = self.image.get_rect()
        self.rect.center = (self.dinosaur.dino_rect.x + 100,self.dinosaur.dino_rect.y + 20)  
        self.speed = 35  
        self.fired = False
        self.hammer = False 

    def update(self, user_input):
        if user_input[pygame.K_SPACE] and not self.fired: 
            self.fired = True
            self.hammer = True
            self.rect.x += self.speed

        
        if self.fired: 
            self.rect.x += self.speed
            if self.rect.x > SCREEN_WIDTH: 
                self.rect.center = (self.dinosaur.dino_rect.x + 100,self.dinosaur.dino_rect.y) 
                self.fired = False


        


    def out_of_screen(self, screen_width, screen_height):
        if self.rect.bottom < 0 or self.rect.top > screen_height or \
           self.rect.right < 0 or self.rect.left > screen_width:
            return True
        else:
            return False
        
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.dinosaur.dino_rect.y))
