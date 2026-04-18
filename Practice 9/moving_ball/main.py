import pygame
import sys
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Ball")

ball = Ball(800, 600)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball.update(keys)

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()