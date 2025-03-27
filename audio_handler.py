import pygame

class AudioHandler:
    """Base class for handling audio in the game."""
    def __init__(self):
        pygame.mixer.init()


class SoundHandler(AudioHandler):
    """Handles sound effects."""
    def __init__(self, sound_path):
        super().__init__()
        self.sound = pygame.mixer.Sound(sound_path)

    def play_bounce(self):
        """Plays the bounce sound effect."""
        self.sound.play()


