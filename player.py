import pygame
from game_entity import GameEntity

class Player(GameEntity):
    #no constructor needed, it uses the parent init function

    def update(self, delta_time, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.x -= 5
        if keys_pressed[pygame.K_RIGHT]:
            self.x += 5
        if keys_pressed[pygame.K_UP]:
            self.y -= 5
        if keys_pressed[pygame.K_DOWN]:
            self.y += 5
        
    def draw(self, screen):
        pygame.draw.rect(screen, (50, 150, 250), (self.x, self.y, 50, 50))
