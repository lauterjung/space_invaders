import pygame

import sys
from classes.ship import Ship


from classes.settings import Settings

class AlienInvasion():
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init
        self.settings = Settings()
        
        # res
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # title
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()