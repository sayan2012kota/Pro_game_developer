import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1000, 800))

yellow_spaceship = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/spaceship_yellow.png")
red_spaceship = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/spaceship_red.png")
space_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/space_background_fight.png")

yellow_spaceship_resize = pygame.transform.scale(yellow_spaceship, (50, 40))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship_resize, (90))
red_spaceship_resize = pygame.transform.scale(red_spaceship, (50, 40))
red_spaceship = pygame.transform.rotate(red_spaceship_resize, (270))

rect = pygame.Rect(495, 0, 10, 800)

def draw_window():
    screen.blit(space_bg, (0,0))
    pygame.draw.rect(screen, "black", rect)
    screen.blit(yellow_spaceship, (200, 400))
    screen.blit(red_spaceship, (800, 400))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()
    draw_window()