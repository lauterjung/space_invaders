from hashlib import new
import imp
import pygame

import sys
from classes.ship import Ship
from classes.bullet import Bullet

from classes.settings import Settings

class AlienInvasion:
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
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        #if event.key == pygame.K_RIGHT:
        #    self.ship.moving_right = True
        #elif event.key == pygame.K_LEFT:
        #    self.ship.moving_left = True
        #el
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # if event.key == pygame.K_RIGHT:
        #    self.ship.moving_right = False
        # elif event.key == pygame.K_LEFT:
        #    self.ship.moving_left = False
        #el 
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        pygame.display.flip()
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()