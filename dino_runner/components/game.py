import pygame

import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,ICON, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player=Dinosaur()
        self.sounds=True
        self.font = pygame.font.Font(None, 30)
        self.time_elapsed = 0
        self.color= True
        self.image_star=ICON
        self.image_cloud=CLOUD
        self.clouds = []
        self.obstacle_manager = ObstacleManager()

        for i in range(3):
            self.clouds.append([random.randint(SCREEN_WIDTH,
             SCREEN_WIDTH + 100), random.randint(50, 200)])



    def run(self):
        self.show_start_screen()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.music()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input= pygame.key.get_pressed()
        
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.time_elapsed +=1
        if  1999 >= self.time_elapsed > 1000:
           self.game_speed=50
           self.color = False
           print(self.color)
        elif 2999 >= self.time_elapsed > 2000:
           self.game_speed=75 
           self.color = True
           print(self.color)
        elif self.time_elapsed > 3000:
           self.game_speed=100 
           self.color = False
           print(self.color)
    

    def music(self):
        if self.sounds == True:
         pygame.mixer.music.load('dino_runner/assets/music/musicadefondo.mp3')
         pygame.mixer.music.play(-1)
         pygame.mixer.music.set_volume(0.3)
        self.sounds= False
     
    def show_start_screen(self):
        self.screen.fill((255, 255, 255))
        start_image =self.image_star 
        start_rect = start_image.get_rect()
        start_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        self.screen.blit(start_image, start_rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render("Presione Enter para jugar", True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.playing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False

    def draw(self):
        self.clock.tick(FPS)
        if self.color == True:
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.player.draw(self.screen)
            time_str = f"SCORE: {self.time_elapsed:012d}"
            time_surface = self.font.render(time_str, True, (0, 0, 0)) 
            self.screen.blit(time_surface, (850, 10))
            self.obstacle_manager.draw(self.screen)
        elif self.color == False:
            self.screen.fill((0, 0, 0))
            self.draw_background()
            self.player.draw(self.screen)
            time_str = f"SCORE: {self.time_elapsed:012d}"
            time_surface = self.font.render(time_str, True, (255, 255, 255)) 
            self.screen.blit(time_surface, (850, 10))
            self.obstacle_manager.draw(self.screen)
        pygame.display.update()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        for cloud in self.clouds:
             self.screen.blit(self.image_cloud, (cloud[0], cloud[1]))

        for cloud in self.clouds:
            cloud[0] -= self.game_speed
        if cloud[0] < -self.image_cloud.get_width():
            self.clouds.remove(cloud)
    
        if len(self.clouds) < 3:
           self.clouds.append([SCREEN_WIDTH, random.randint(50, 200)])

