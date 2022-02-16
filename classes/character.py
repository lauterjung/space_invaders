import pygame

class Character:
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/crash.png')
        self.rect = self.image.get_rect()
        
        self.small_image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.small_image.get_rect()
        
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.small_image, self.rect)