import pygame

import sys

from classes.settings import Settings

class TextInput:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init
        self.settings = Settings()
        
        # res
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # title
        pygame.display.set_caption("Text input")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()
        
if __name__ == '__main__':
    ai = TextInput()
    ai.run_game()