import pygame

from dino_runner.utils.constants import  FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
     half_screen_height= SCREEN_HEIGHT // 2
     half_screen_width= SCREEN_WIDTH // 2

     def __init__(self, message, screen):
        self.menu_end = False
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect= self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)
        self.text_2 = None
        self.text_4 = None
        self.text_time = None


     def update(self,game):
       pygame.display.update()
       self.handle_events_on_menu(game)

     def draw(self, screen):
      screen.blit(self.text,self.text_rect)
      if self.menu_end == True:
         screen.blit(self.text_game_over,self.text_game_over_rect)
         screen.blit(self.text_1,self.text_rect1)
         if self.text_2:   
            screen.blit(self.text_2,self.text_rect_2)
            screen.blit(self.text_3, self.text_rect_3)
            if self.text_4:   
               screen.blit(self.text_4,self.text_rect_4)
               screen.blit(self.text_5, self.text_rect_5)

     def reset_screen_color(self, screen):
      screen.fill((255, 255, 255))

     def handle_events_on_menu(self, game):
       for event in pygame.event.get():
         if (event.type == pygame.QUIT):
           game.running = False
           game.playing = False
         elif event.type == pygame.KEYDOWN:
           game.run()

     def update_message(self, message,points):
       self.menu_end = True
       self.text_game_over =self. font.render("GAME OVER. PRESS ANY KEY TO STARD", True, (0,0,0))
       self.text_game_over_rect = self.text_game_over.get_rect()
       self.text_game_over_rect.center = (self.half_screen_width, self.half_screen_height - 200)
       self.text = self. font.render(message, True, (0,0,0))
       self.text_rect = self.text.get_rect()
       self.text_rect.center = (self.half_screen_width, self.half_screen_height)
       self.text_1 = self. font.render(str(points), True, (0,0,0))
       self.text_rect1= self.text_1.get_rect()
       self.text_rect1.center = (self.half_screen_width + 80, self.half_screen_height)

     def update_message_2(self, message_2, Points_1):
       self.menu_end = True
       self.text_2 = self.font.render(message_2, True, (0, 0, 0))
       self.text_rect_2 = self.text_2.get_rect()
       self.text_rect_2.center = (self.half_screen_width - 10, self.half_screen_height + 50)
       self.text_3 = self. font.render(str(Points_1), True, (0,0,0))
       self.text_rect_3= self.text_3.get_rect()
       self.text_rect_3.center = (self.half_screen_width + 90, self.half_screen_height + 50)

     def update_message_3(self, message_3, points_2):
       self.menu_end = True
       self.text_4 = self.font.render(message_3, True, (0, 0, 0))
       self.text_rect_4 = self.text_4.get_rect()
       self.text_rect_4.center = (self.half_screen_width - 10, self.half_screen_height + 100)
       self.text_5 = self. font.render(str(points_2), True, (0,0,0))
       self.text_rect_5= self.text_5.get_rect()
       self.text_rect_5.center = (self.half_screen_width + 120, self.half_screen_height + 100)

     def  update_time(self, message):
       self.menu_end = True
       self.text_time = self.font.render(message, True, (0,0,0))
       self.text_time_rect = self.text_time.get_rect()
       self.text_time_rect.center = (self.half_screen_width, self.half_screen_height - 200)
     def draw_1(self,screen):
      if self.text_time:
         screen.blit(self.text_time,self.text_time_rect)
       

             

