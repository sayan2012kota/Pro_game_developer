from pygame.locals import *
import pygame
from time import *
pygame.init()

screen = pygame.display.set_mode((700, 500))

rocket = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/rocket_image.png")
space_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/space_background.png")

keys = [False, False, False, False]

x = 350
y = 250

while True:
    screen.blit(space_bg, (0,0))
    screen.blit(rocket, (x, y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_RIGHT:
                keys[1] = True
            elif event.key == K_LEFT:
                keys[2] = True
            elif  event.key == K_DOWN:
                keys[3] = True
        if event.type == KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_RIGHT:
                keys[1] = False
            elif event.key == K_LEFT:
                keys[2] = False
            elif  event.key == K_DOWN:
                keys[3] = False
            
    if keys[0]:
        y = y - 5
    elif keys[1]:
        if x < 575:
            x = x + 5 
    elif keys[2]:
        if x > -25:
            x = x - 5  
    
    y = y + 1 
    sleep(0.05)
    

    
