import pygame
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((1000, 800))

bullet_hit_sound = pygame.mixer.Sound("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/Gun+Silencer.mp3")
bullet_fire_sound = pygame.mixer.Sound("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/Grenade+1.mp3")

yellow_spaceship = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/spaceship_yellow.png")
red_spaceship = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/spaceship_red.png")
space_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/space_background_fight.png")

yellow_spaceship_resize = pygame.transform.scale(yellow_spaceship, (50, 40))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship_resize, (90))
red_spaceship_resize = pygame.transform.scale(red_spaceship, (50, 40))
red_spaceship = pygame.transform.rotate(red_spaceship_resize, (270))
H_font = pygame.font.SysFont("Calibra", 40)

rect = pygame.Rect(495, 0, 10, 800)
yellow_bullet_hit = pygame.USEREVENT+1
red_bullet_hit = pygame.USEREVENT+2

def draw_window(Y_rect, R_rect, R_bullets, Y_bullets):
    screen.blit(space_bg, (0,0))
    pygame.draw.rect(screen, "black", rect)
    screen.blit(yellow_spaceship, (Y_rect.x, Y_rect.y))
    screen.blit(red_spaceship, (R_rect.x, R_rect.y))
    Yellow_health_text = H_font.render("HEALTH: "+str(Y_health), 1, "white")
    Red_health_text = H_font.render("HEALTH: "+str(R_health), 1, "white")
    screen.blit(Yellow_health_text, (10, 10))
    screen.blit(Red_health_text, (820, 10))
    for bullet in R_bullets:
        pygame.draw.rect(screen, "red", bullet)
    for bullet2 in Y_bullets:
        pygame.draw.rect(screen, "yellow", bullet2)
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

def move_bullets(Y_bullets, R_bullets, Y_rect, R_rect):
    for bullet in Y_bullets:
        bullet.x = bullet.x + velocity
        if bullet.colliderect(R_rect):
            pygame.event.post(pygame.event.Event(yellow_bullet_hit))
            Y_bullets.remove(bullet)
        elif bullet.x > 1000:
            Y_bullets.remove(bullet)
    for bullet in R_bullets:
        bullet.x = bullet.x - velocity
        if bullet.colliderect(Y_rect):
            pygame.event.post(pygame.event.Event(red_bullet_hit))
            R_bullets.remove(bullet)
        elif bullet.x < 0:
            R_bullets.remove(bullet)

Y_health = 10
R_health = 10
clock = pygame.time.Clock()
Y_rect = pygame.Rect(200, 400, 50, 40)
R_rect = pygame.Rect(800, 400, 50, 40)

max_bullets = 8
velocity = 8

yellow_health = 10
red_health = 10

winner = ""

Y_bullets = []
R_bullets = []

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LCTRL and len(R_bullets) < max_bullets:
                bullet = pygame.Rect(R_rect.x, R_rect.y + 20, 10, 5)
                R_bullets.append(bullet)
                bullet_fire_sound.play()
            if event.key == K_RCTRL and len(Y_bullets) < max_bullets:
                bullet2 = pygame.Rect(Y_rect.x + 40, Y_rect.y + 20, 10, 5)
                Y_bullets.append(bullet2)
                bullet_fire_sound.play()
        if event.type == red_bullet_hit:
            Y_health = Y_health - 1
            bullet_hit_sound.play()
        if event.type == yellow_bullet_hit:
            R_health = R_health - 1
            bullet_hit_sound.play()
    if R_health <= 0:
        winner = "yellow spaceship wins"
        text_colour = "yellow"
    if Y_health <= 0:
        winner = "red spaceship wins"
        text_colour = "red"
    if winner != "":
        wintext = H_font.render(winner, 1, text_colour) 
        screen.blit(wintext, (500, 400)) 
        pygame.display.update()
        pygame.time.delay(6000) 
        break    
    key_press = pygame.key.get_pressed()
    move_bullets(Y_bullets, R_bullets, Y_rect, R_rect)

    move_y(key_press, Y_rect)
    move_r(key_press, R_rect)
    draw_window(Y_rect, R_rect, R_bullets, Y_bullets)
    pygame.display.update()