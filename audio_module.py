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

    def play_sound(self):
        """Plays the bounce sound effect."""
        self.sound.play()


class MusicHandler(AudioHandler):
    """Handles background music."""
    def __init__(self, music: str):
        super().__init__()
        self.background_music = pygame.mixer.music
        self.background_music.load(background_music)
        self.background_music.play(-1)

    def change_music(self, new_music):
        """Stops current playing music, and starts a new one"""
        self.background_music.fadeout(1000)
        self.background_music.unload()
        self.background_music.load(new_music)
        self.background_music.play(-1)

    def toggle_music(self):
        """Plays or Pauses background music."""
        if not self.background_music.get_busy:
            self.background_music.unpause()
        else:
            self.background_music.pause()
