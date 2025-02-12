import pygame
import sys
from player import Player
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("BULLET HELL")
clock = pygame.time.Clock() # controls frame rates

blue = (0, 71, 171)

p1 = Player(400, 400, blue, 50, 50)
e1 = [Enemy(50, 50, "linear"), Enemy(50, 50, "circular")]

bullets = []

def main():
    running = True
    clock.tick(60)
    while running: #GAME LOOP####################################
        #event section------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        #update section-----------------------------------
        delta_time = clock.tick(60)/1000 

        p1.update(delta_time, keys)

        for j in e1:
            j.update(delta_time, bullets)

        for bullet in bullets[:]: #iterate through a copy of the list
            bullet.update(delta_time)
            if not bullet.alive:
                bullets.remove(bullet)

        #render section-----------------------------------
        screen.fill((0, 0, 0))

        p1.draw(screen)

        for i in e1:
            i.draw(screen)

        for k in e1:
            k.shoot(bullets)

        pygame.display.flip()

    #end of GAME LOOP##############################################
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
