import sys
import pygame
from pathlib import Path

from text_module import VerticalMoveText, HorizontalMoveText, BounceText
from audio_module import MusicPlaylist
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, FPS, BACKGROUND_MUSIC_PATH

class Game:
    """Main class for the DVD simulation game."""

    def __init__(self):
        """Initializes the game, setting up the screen, clock, and background music."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('DVD')
        self.clock = pygame.time.Clock()
        self.running = True
        self.text = BounceText("Samuel", 50, WHITE, './sounds/bounce.mp3', 5, 5)

        # Load background music playlist
        self.background_music = MusicPlaylist(
            [BACKGROUND_MUSIC_PATH + f.name for f in Path(BACKGROUND_MUSIC_PATH).iterdir()]
        )
        self.background_music.music.play(-1)

    def handle_events(self):
        """Handles user input events, such as quitting and key presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYUP:
                self.handle_key_press(event)

    def handle_key_press(self, event):
        """Handles key press events to control game actions.

        - ESC: Quit the game.
        - SPACE: Toggle background music (play/pause).
        - S: Skip to the next track in the playlist.
        """
        if event.key == pygame.K_ESCAPE:
            self.running = False

        if event.key == pygame.K_SPACE:
            self.background_music.music_player.toggle_music()

        if event.key == pygame.K_s:
            self.background_music.next_music()
            self.background_music.music.play(-1)

    def update_text_position(self):
        """Updates the position of the bouncing text."""
        self.text.update()

    def draw_screen(self):
        """Renders the screen, clears it, draws the text, and updates the display."""
        self.screen.fill(BLACK)
        self.text.draw(self.screen)
        pygame.display.flip()        

    def run(self):
        """Main game loop. Handles events, updates the text, and redraws the screen."""
        while self.running:
            self.handle_events()
            self.update_text_position()
            self.draw_screen()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()
