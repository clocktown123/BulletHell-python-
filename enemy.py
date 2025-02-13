import pygame
import math
from game_entity import GameEntity
from bullet import Bullet

class Enemy(GameEntity):
    def __init__(self, x, y, movement_pattern = "circular", shoot_interval = 2):
        super().__init__(x, y, (250, 50, 50), 20, 20) #parent class constructor
        self.movement_pattern = movement_pattern
        self.speed = 50
        self.angle = 0
        self.direction = 1
        self.shoot_interval = shoot_interval #cd for shooting bullets
        self.time_since_last_shot = 0
    
    def update(self, delta_time, bullets):
        self.time_since_last_shot += delta_time
        #movement for enemy
        if self.movement_pattern == "linear":
            self.x += self.speed * self.direction * delta_time
            if self.x < 0 or self.x +self.width > 800: # reverse the direction when at bounds
                self.direction *= -1
        elif self.movement_pattern == "circular":
            #print("yo")
            self.angle += self.speed * delta_time/200 #200 is the radius of the circle we're moving around
            self.x = 400 + math.cos(self.angle)*200 #(400, 300) is the center of the circle we're moving around
            self.y = 300 + math.sin(self.angle)*200
        #add more patterns here

        #shoot bullets
        if self.time_since_last_shot >= self.shoot_interval:
            self.shoot(bullets)
            self.time_since_last_shot = 0
        
    def shoot(self, bullets):
        num_bullets = 100 #adjust this for more or less particles on screen
        angle_step = 2 * math.pi/num_bullets
        for i in range(num_bullets):
            angle = i * angle_step
            bullets.append(Bullet((i%255, i%100, 150), self.x+self.width/2, self.y+self.height/2, 100, angle, 'square'))
        

    #def draw(self, screen):
       #return super().draw(screen)
