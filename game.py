import sys
import pygame


from text_module import VerticalMoveText, HorizontalMoveText, BounceText
from config import SCREEN_WIDTH,SCREEN_HEIGHT,BLACK,WHITE,FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('DVD')
        self.clock = pygame.time.Clock()
        self.running = True
        self.text = BounceText("Samuel", 50, WHITE, './sounds/bounce.mp3', 5, 5)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYUP:
                self.handle_key_press(event)
    
    def handle_key_press(self, event):
        if event.key == pygame.K_ESCAPE:
            self.running = False

        if event.key == pygame.K_SPACE:
            self.running = False

                        
    def update_text_position(self):
        self.text.update()
    
    def draw_screen(self):
        self.screen.fill(BLACK)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update_text_position()
            self.draw_screen()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()