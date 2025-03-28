import pygame

class AudioHandler:
    """Base class for handling audio in the game."""
    
    def __init__(self):
        """Initializes the audio mixer."""
        pygame.mixer.init()


class SoundHandler(AudioHandler):
    """Handles sound effects."""

    def __init__(self, sound_path: str):
        """Loads a sound effect from the given file path.
        
        Args:
            sound_path (str): Path to the sound effect file.
        """
        super().__init__()
        self.sound = pygame.mixer.Sound(sound_path)

    def play_sound(self):
        """Plays the loaded sound effect."""
        self.sound.play()


class MusicHandler(AudioHandler):
    """Handles background music playback."""

    def __init__(self, music: str):
        """Loads and plays background music on loop.
        
        Args:
            music (str): Path to the background music file.
        """
        super().__init__()
        self.music = pygame.mixer.music
        self.music.load(music)
        self.music.play(-1)        

    def toggle_music(self):
        """Toggles between playing and pausing background music."""
        if not self.music.get_busy():
            self.music.unpause()
        else:
            self.music.pause()


class MusicPlaylist:
    """Manages a playlist of background music tracks."""

    def __init__(self, playlist: list[str]):
        """Initializes the playlist and starts playing the first track.
        
        Args:
            playlist (list[str]): List of music file paths.
        """
        super().__init__()
        self.playlist = playlist
        self.music_index = 0        
        self.music_player = MusicHandler(self.playlist[self.music_index])
        self.music = self.music_player.music

    def change_music(self, new_music: str):
        """Stops the current music and starts a new one.
        
        Args:
            new_music (str): Path to the new music file.
        """
        self.music.unload()
        self.music.load(new_music)

    def next_music(self):
        """Advances to the next track in the playlist, looping if necessary."""
        self.music_index = (self.music_index + 1) % len(self.playlist)
        self.change_music(self.playlist[self.music_index])
