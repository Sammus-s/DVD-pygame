import pygame
import random

from config import MAX_SPEED, MIN_SPEED

class MoveText:
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center = (screen_width/2, screen_height/2))        
        
        self.speed_x = self._get_random_velocity()
        self.speed_y = self._get_random_velocity()

        self.screen_height = screen_height
        self.screen_width = screen_width

        
    def _get_random_velocity(self, current_speed = 0):
        random_velocity = random.randint(MIN_SPEED, MAX_SPEED)
        
        if current_speed < 0:
            return random_velocity
        else:
            return -random_velocity

    
    def _set_random_color(self):
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.text_surf = self.font.render(self.text, True, self.color)
            
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y        
            
        if self.rect.left <= 0:
            self.speed_x = self._get_random_velocity(self.speed_x)
            self.rect.left = 0            
            self._set_random_color()
        elif self.rect.right >= self.screen_width:
            self.speed_x = self._get_random_velocity(self.speed_x)
            self.rect.right = self.screen_width
            self._set_random_color()
        
        if self.rect.top <= 0:
            self.speed_y = self._get_random_velocity(self.speed_y)
            self.rect.top = 0
            self._set_random_color()
        elif self.rect.bottom >= self.screen_height:
            self.speed_y = self._get_random_velocity(self.speed_y)
            self.rect.bottom = self.screen_height
            self._set_random_color()

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)
        
