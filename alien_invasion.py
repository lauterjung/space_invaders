import pygame

import sys
from classes.character import Character
from classes.ship import Ship


from classes.settings import Settings

class AlienInvasion:
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
        self.character = Character(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):                
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.character.blitme()

        pygame.display.flip()
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()