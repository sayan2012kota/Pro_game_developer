import pygame
from pygame.locals import *
pygame.font.init()
pygame.init()

screen = pygame.display.set_mode((1000, 800))

yellow_spaceship = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/spaceship_yellow.png")
red_spaceship = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/spaceship_red.png")
space_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/space_background_fight.png")

yellow_spaceship_resize = pygame.transform.scale(yellow_spaceship, (50, 40))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship_resize, (90))
red_spaceship_resize = pygame.transform.scale(red_spaceship, (50, 40))
red_spaceship = pygame.transform.rotate(red_spaceship_resize, (270))
H_font = pygame.font.SysFont("Calibra", 40)

rect = pygame.Rect(495, 0, 10, 800)

def draw_window(Y_rect, R_rect):
    screen.blit(space_bg, (0,0))
    pygame.draw.rect(screen, "black", rect)
    screen.blit(yellow_spaceship, (Y_rect.x, Y_rect.y))
    screen.blit(red_spaceship, (R_rect.x, R_rect.y))
    Yellow_health_text = H_font.render("HEALTH: "+str(Y_health), 1, "white")
    Red_health_text = H_font.render("HEALTH: "+str(R_health), 1, "white")
    screen.blit(Yellow_health_text, (10, 10))
    screen.blit(Red_health_text, (820, 10))
    pygame.display.update()
    
def move_y(key_press, Y_rect):
    if key_press[pygame.K_LEFT] and Y_rect.x > 0:
        Y_rect.x = Y_rect.x - 10
    if key_press[pygame.K_RIGHT] and Y_rect.x < 495:
        Y_rect.x = Y_rect.x + 10
    if key_press[pygame.K_UP] and Y_rect.y > 0:
        Y_rect.y = Y_rect.y - 10
    if key_press[pygame.K_DOWN] and Y_rect.y < 800:
        Y_rect.y = Y_rect.y + 10

def move_r(red_keys, R_rect):
    if red_keys[pygame.K_a] and R_rect.x > 505:
        R_rect.x = R_rect.x - 10
    if red_keys[pygame.K_d] and R_rect.x < 1000:
        R_rect.x = R_rect.x + 10
    if red_keys[pygame.K_w] and R_rect.y > 0:
        R_rect.y = R_rect.y - 10
    if red_keys[pygame.K_s] and R_rect.y < 800:
        R_rect.y = R_rect.y + 10

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    key_press = pygame.key.get_pressed()
    Y_rect = pygame.Rect(200, 400, 50, 40)
    R_rect = pygame.Rect(800, 400, 50, 40)
    Y_health = 10
    R_health = 10
    move_y(key_press, Y_rect)
    move_r(key_press, R_rect)
    draw_window(Y_rect, R_rect)
    pygame.display.update()