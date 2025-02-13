import pygame
import math
from game_entity import GameEntity


class Bullet(GameEntity):
    def __init__(self, color, x, y, speed, angle, pattern):
        super().__init__(x, y, (200, 200, 50), 5, 5)
        self.speed = speed
        self.angle = angle
        self.pattern = pattern
        self.color = color
        self.alive = True

    def update(self, delta_time):
        self.angle += .01 * delta_time

        if self.pattern == 'square':
            self.x += math.sin(self.angle*3) * self.speed * delta_time
            self.y += math.sin(self.angle*4) * self.speed * delta_time
        
        if self.pattern == 'flower':
            self.x += math.sin(self.angle)-math.cos(self.angle*10) * self.speed * delta_time
            self.y += math.cos(self.angle)-math.sin(self.angle*10) * self.speed * delta_time
        #add more patterns here

        if not (0 <= self.x <= 800 and 0 <= self.y <= 800): #check the bounds and kill bullets off screen
            self.alive = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
