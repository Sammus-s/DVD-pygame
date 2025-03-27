import pygame
from abc import ABC, abstractmethod
import random

from config import MAX_SPEED, MIN_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from color_module import ColorGenerator

class MoveText:
    def __init__(self, text, font_size, text_color):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = text_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))        
    
    def _set_random_color(self):
        self.color = ColorGenerator.get_random_color()
        self.text_surf = self.font.render(self.text, True, self.color)
    
    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)

    @abstractmethod
    def update(self):
        pass


class HorizontalMoveText(MoveText):
    def __init__(self, text, font_size, text_color, speed_y):
        super().__init__(text, font_size, text_color)
        self.speed_y = speed_y    
    
    def update(self):
        self.rect.y = max(0, min((self.rect.y + self.speed_y), SCREEN_HEIGHT - self.rect.height))
        is_colliding_y = self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT

        if is_colliding_y:
            self.speed_y *= -1
            self._set_random_color()


class VerticalMoveText(MoveText):
    def __init__(self, text, font_size, text_color, speed_x):
        super().__init__(text, font_size, text_color)
        self.speed_x = speed_x    
    
    def update(self):
        self.rect.x = max(0, min((self.rect.x + self.speed_x), SCREEN_WIDTH - self.rect.width))
        is_colliding_x = self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH

        if is_colliding_x:
            self.speed_x *= -1
            self._set_random_color()
        

class BounceText(MoveText):
    def __init__(self, text, font_size, text_color, speed_y, speed_x):
        super().__init__(text, font_size, text_color)
        self.speed_y = speed_y   
        self.speed_x = speed_x  
    
    def update(self):
        self.rect.y = max(0, min((self.rect.y + self.speed_y), SCREEN_HEIGHT - self.rect.height))
        self.rect.x = max(0, min((self.rect.x + self.speed_x), SCREEN_WIDTH - self.rect.width))

        is_colliding_x = self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH
        is_colliding_y = self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT

        if is_colliding_y:
            self.speed_y *= -1            
        if is_colliding_x:
            self.speed_x *= -1
        
        if is_colliding_x or is_colliding_y:
            self._set_random_color()
        