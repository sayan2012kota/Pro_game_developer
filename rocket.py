from pygame.locals import *
import pygame
pygame.init()

screen = pygame.display.set_mode((700, 500))



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
