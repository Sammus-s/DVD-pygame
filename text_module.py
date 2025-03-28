import pygame
from abc import ABC, abstractmethod
import random

from config import MAX_SPEED, MIN_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from color_module import ColorGenerator
from audio_module import SoundHandler

class MoveText(ABC):
    """Base class for handling text movement with bounce effects."""

    def __init__(self, text: str, font_size: int, text_color: tuple, bounce_sound: str):
        """Initializes the text, font, color, and bounce sound effect.
        
        Args:
            text (str): The text to display.
            font_size (int): The font size of the text.
            text_color (tuple): The color of the text in RGB format.
            bounce_sound (str): Path to the bounce sound effect.
        """
        self.font = pygame.font.SysFont(None, font_size)
        self.color = text_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))        
        self.bounce_effect = SoundHandler(bounce_sound)
    
    def _set_random_color(self):
        """Sets a random color for the text."""
        self.color = ColorGenerator.get_random_color()
        self.text_surf = self.font.render(self.text, True, self.color)
    
    def draw(self, screen):
        """Draws the text on the screen at its current position.
        
        Args:
            screen (Surface): The Pygame screen to draw the text on.
        """
        screen.blit(self.text_surf, self.rect)

    @abstractmethod
    def update(self):
        """Abstract method to update the text position. To be implemented in subclasses."""
        pass

    @abstractmethod
    def bounce_on_colision(self):
        """Abstract method to handle text bounce when a collision occurs. To be implemented in subclasses."""
        pass


class HorizontalMoveText(MoveText):
    """Handles horizontal movement of text and bounce effects."""

    def __init__(self, text: str, font_size: int, text_color: tuple, bounce_sound: str, speed_y: int):
        """Initializes the horizontal movement text.
        
        Args:
            text (str): The text to display.
            font_size (int): The font size of the text.
            text_color (tuple): The color of the text in RGB format.
            bounce_sound (str): Path to the bounce sound effect.
            speed_y (int): The speed at which the text moves vertically.
        """
        super().__init__(text, font_size, text_color, bounce_sound)
        self.speed_y = speed_y    
    
    def update(self):
        """Updates the position of the text on the screen, ensuring it stays within bounds."""
        self.rect.y = max(0, min((self.rect.y + self.speed_y), SCREEN_HEIGHT - self.rect.height))
        self.bounce_on_colision()
    
    def bounce_on_colision(self):
        """Handles the bounce effect when the text collides with the top or bottom of the screen."""
        is_colliding_y = self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT

        if is_colliding_y:
            self.speed_y *= -1
            self._set_random_color()
            self.bounce_effect.play_sound()


class VerticalMoveText(MoveText):
    """Handles vertical movement of text and bounce effects."""

    def __init__(self, text: str, font_size: int, text_color: tuple, bounce_sound: str, speed_x: int):
        """Initializes the vertical movement text.
        
        Args:
            text (str): The text to display.
            font_size (int): The font size of the text.
            text_color (tuple): The color of the text in RGB format.
            bounce_sound (str): Path to the bounce sound effect.
            speed_x (int): The speed at which the text moves horizontally.
        """
        super().__init__(text, font_size, text_color, bounce_sound)
        self.speed_x = speed_x    
    
    def update(self):
        """Updates the position of the text on the screen, ensuring it stays within bounds."""
        self.rect.x = max(0, min((self.rect.x + self.speed_x), SCREEN_WIDTH - self.rect.width))
        self.bounce_on_colision()
    
    def bounce_on_colision(self):
        """Handles the bounce effect when the text collides with the left or right of the screen."""
        is_colliding_x = self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH

        if is_colliding_x:
            self.speed_x *= -1
            self._set_random_color()
            self.bounce_effect.play_sound()
        

class BounceText(MoveText):
    """Handles text that moves in both directions (horizontal and vertical) with bounce effects."""

    def __init__(self, text: str, font_size: int, text_color: tuple, bounce_sound: str, speed_y: int, speed_x: int):
        """Initializes the bouncing text.
        
        Args:
            text (str): The text to display.
            font_size (int): The font size of the text.
            text_color (tuple): The color of the text in RGB format.
            bounce_sound (str): Path to the bounce sound effect.
            speed_y (int): The vertical speed of the text.
            speed_x (int): The horizontal speed of the text.
        """
        super().__init__(text, font_size, text_color, bounce_sound)
        self.speed_y = speed_y   
        self.speed_x = speed_x

    def bounce_text(self):
        """Reverses both the horizontal and vertical movement speeds."""
        self.speed_y = -self.speed_y   
        self.speed_x = -self.speed_x
        self.bounce_effect.play_sound()

    def update(self):
        """Updates the position of the text, ensuring it stays within bounds and occasionally bounces."""
        self.rect.y = max(0, min((self.rect.y + self.speed_y), SCREEN_HEIGHT - self.rect.height))
        self.rect.x = max(0, min((self.rect.x + self.speed_x), SCREEN_WIDTH - self.rect.width))
        self.bounce_on_colision()

        if random.randint(0, 101) == 0:  # Randomly reverse the direction
            self.bounce_text()
        
    def bounce_on_colision(self):
        """Handles the bounce effect when the text collides with any of the screen edges."""
        is_colliding_x = self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH
        is_colliding_y = self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT

        if is_colliding_y:
            self.speed_y *= -1            
        if is_colliding_x:
            self.speed_x *= -1
        
        if is_colliding_x or is_colliding_y:
            self._set_random_color()
            self.bounce_effect.play_sound()
