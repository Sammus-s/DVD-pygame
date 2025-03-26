import pygame
from abc import ABC, abstractmethod
import random

from config import MAX_SPEED, MIN_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH

class MoveText:
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

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)
        
