import pygame
pygame.init()
HEIGHT=500
WIDTH=500
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("red")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()