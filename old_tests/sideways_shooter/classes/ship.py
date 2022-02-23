import pygame

class Ship:
    

    
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rotated_image = pygame.transform.rotate(pygame.image.load('images/ship.bmp'), 90)
        self.rect = self.rotated_image.get_rect()
        # self.rect = self.image.get_rect()
        
        self.rect.midleft = self.screen_rect.midleft
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
                
        # Movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False     
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
                            
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(pygame.transform.rotate(self.image, -90), self.rect)
        