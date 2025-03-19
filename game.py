import sys
import pygame
from dvd import MoveText
from config import SCREEN_WIDTH,SCREEN_HEIGHT,BLACK,WHITE,FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('DVD')
        self.clock = pygame.time.Clock()
        self.running = True
        self.text = MoveText("Samuel", 50, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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