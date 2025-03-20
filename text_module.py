import pygame
import random

from config import MAX_SPEED, MIN_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH

class DVDText:
    def __init__(self, text, font_size, text_color):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = text_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))        
    
    def _set_random_color(self):
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.text_surf = self.font.render(self.text, True, self.color)

    @abstractmethod
    def update(self):
        pass


class MoveText(DVDText):
    def super.__init__(self, text, font_size, text_color):
        self.obj_text.speed_x = self._get_random_velocity()
        self.obj_text.speed_y = self._get_random_velocity()

        
    def _get_random_velocity(self, current_speed = 0):
        random_velocity = random.randint(MIN_SPEED, MAX_SPEED)
        if current_speed < 0:
            return random_velocity
        else:
            return -random_velocity
    
    def update(self):
        self.obj_text.rect.x += self.obj_text.speed_x
        self.obj_text.rect.y += self.obj_text.speed_y
            
        if self.obj_text.rect.left <= 0:
            self.obj_text.speed_x = self.obj_text._get_random_velocity(self.obj_text.speed_x)
            self.obj_text.rect.left = 0
            self.obj_text._set_random_color()
        elif self.obj_text.rect.right >= self.obj_text.screen_width:
            self.obj_text.speed_x = self.obj_text._get_random_velocity(self.obj_text.speed_x)
            self.obj_text.rect.right = self.obj_text.screen_width
            self.obj_text._set_random_color()
        
        if self.obj_text.rect.top <= 0:
            self.obj_text.speed_y = self.obj_text._get_random_velocity(self.obj_text.speed_y)
            self.obj_text.rect.top = 0
            self.obj_text._set_random_color()
        elif self.obj_text.rect.bottom >= self.obj_text.screen_height:
            self.obj_text.speed_y = self.obj_text._get_random_velocity(self.obj_text.speed_y)
            self.obj_text.rect.bottom = self.obj_text.screen_height
            self.obj_text._set_random_color()

    def draw(self, screen):
        screen.blit(self.obj_text.text_surf, self.obj_text.rect)
        
