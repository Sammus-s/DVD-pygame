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
    def __init__(self, music):
        super().__init__()
        self.music = pygame.mixer.music
        self.music.load(music)
        self.music.play(-1)        

    def toggle_music(self):
        """Plays or Pauses background music."""
        if not self.music.get_busy():
            self.music.unpause()
        else:
            self.music.pause()

class MusicPlaylist():
    
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist
        self.music_index = 0        
        self.music_player = MusicHandler(self.playlist[self.music_index])
        self.music = self.music_player.music

    def change_music(self, new_music):
        """Stops current playing music, and starts a new one"""
        self.music.unload()
        self.music.load(new_music)

    def next_music(self):
        self.music_index = (self.music_index + 1) % len(self.playlist)
        self.change_music(self.playlist[self.music_index])
