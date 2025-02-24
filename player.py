import pygame
import math
from game_entity import GameEntity
from missile import Missile

class Player(GameEntity):
    def __init__(self, x, y, shoot_interval = 1):
        super().__init__(x, y, (250, 50, 50), 20, 20) #parent class constructor

        self.angle = 0
        self.direction = 1
        self.shoot_interval = shoot_interval #cd for shooting bullets
        self.time_since_last_shot = 0

    def update(self, delta_time, keys_pressed, missiles):
        self.time_since_last_shot += delta_time

        if keys_pressed[pygame.K_LEFT]:
            self.x -= 5
        if keys_pressed[pygame.K_RIGHT]:
            self.x += 5
        if keys_pressed[pygame.K_UP]:
            self.y -= 5
        if keys_pressed[pygame.K_DOWN]:
            self.y += 5

        if self.time_since_last_shot >= self.shoot_interval:
            self.shoot(missiles)
            self.time_since_last_shot = 0

        
        
    def draw(self, screen):
        pygame.draw.rect(screen, (102, 255, 0), (self.x, self.y, 5, 5))

    def shoot(self, missiles):
        num_missiles = 100 #adjust this for more or less particles on screen
        angle_step = 2 * math.pi/num_missiles
        for i in range(num_missiles):
            angle = i * angle_step
            missiles.append(Missile((255, 10, 10), self.x+self.width/2, self.y+self.height/2, 100, angle, 'flower'))
