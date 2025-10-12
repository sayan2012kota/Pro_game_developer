import pygame
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
pygame.init()

screen  = pygame.display.set_mode((1000, 800))

bullet_hit_sound = pygame.mixer.Sound("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/Gun+Silencer.mp3")
bullet_fire_sound = pygame.mixer.Sound("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/Grenade+1.mp3")


green_submarine = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/green_submarine(game).png")
blue_submarine = pygame.image.load("C:/Users/pooja\Desktop/pro_game_development/Game_developer2/lesson_2/blue_submarine(game).png")
ocean_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/ocean_bg.jpg")

green_submarine_resize = pygame.transform.scale(green_submarine, (50, 40))
blue_submarine_resize = pygame.transform.scale(blue_submarine, (50, 40))
ocean_bg_resize = pygame.transform.scale(ocean_bg, (1000, 800))
H_font = pygame.font.SysFont("Calibra", 40)

rect = pygame.Rect(495, 0, 10, 800)
green_bullet_hit = pygame.USEREVENT+1
blue_bullet_hit = pygame.USEREVENT+2

def draw_window(G_rect, B_rect, G_bullets, B_bullets):
    screen.blit(ocean_bg_resize, (0,0))
    pygame.draw.rect(screen, "black", rect)
    screen.blit(green_submarine_resize, (G_rect.x, G_rect.y))
    screen.blit(blue_submarine_resize, (B_rect.x, B_rect.y))
    Green_health_text = H_font.render("HEALTH: "+str(G_health), 1, "green")
    Blue_health_text = H_font.render("HEALTH: "+str(B_health), 1, "blue")
    screen.blit(Green_health_text, (10, 10))
    screen.blit(Blue_health_text, (820, 10))
    for bullet in B_bullets:
        pygame.draw.rect(screen, "blue", bullet)
    for bullet2 in G_bullets:
        pygame.draw.rect(screen, "green", bullet2)
    pygame.display.update()
    
def move_g(key_press, G_rect):
    if key_press[pygame.K_LEFT] and G_rect.x > 0:
        G_rect.x = G_rect.x - 10
    if key_press[pygame.K_RIGHT] and G_rect.x < 495:
        G_rect.x = G_rect.x + 10
    if key_press[pygame.K_UP] and G_rect.y > 0:
        G_rect.y = G_rect.y - 10
    if key_press[pygame.K_DOWN] and G_rect.y < 800:
        G_rect.y = G_rect.y + 10

def move_b(key_press2, B_rect):
    if key_press2[pygame.K_a] and B_rect.x > 505:
        B_rect.x = B_rect.x - 10
    if key_press2[pygame.K_d] and B_rect.x < 1000:
        B_rect.x = B_rect.x + 10
    if key_press2[pygame.K_w] and B_rect.y > 0:
        B_rect.y = B_rect.y - 10
    if key_press2[pygame.K_s] and B_rect.y < 800:
        B_rect.y = B_rect.y + 10

def move_bullets(G_bullets, B_bullets, G_rect, B_rect):
    for bullet in G_bullets:
        bullet.x = bullet.x + velocity
        if bullet.colliderect(B_rect):
            pygame.event.post(pygame.event.Event(green_bullet_hit))
            G_bullets.remove(bullet)
        elif bullet.x > 1000:
            G_bullets.remove(bullet)
    for bullet in B_bullets:
        bullet.x = bullet.x - velocity
        if bullet.colliderect(G_rect):
            pygame.event.post(pygame.event.Event(blue_bullet_hit))
            B_bullets.remove(bullet)
        elif bullet.x < 0:
            B_bullets.remove(bullet)

G_health = 10
B_health = 10
clock = pygame.time.Clock()
G_rect = pygame.Rect(200, 400, 50, 40)
B_rect = pygame.Rect(800, 400, 50, 40)

max_bullets = 8
velocity = 8

green_health = 10
blue_health = 10

winner = ""

G_bullets = []
B_bullets = []

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LCTRL and len(B_bullets) < max_bullets:
                bullet = pygame.Rect(B_rect.x, B_rect.y + 20, 10, 5)
                B_bullets.append(bullet)
                bullet_fire_sound.play()
            if event.key == K_RCTRL and len(G_bullets) < max_bullets:
                bullet2 = pygame.Rect(G_rect.x + 40, G_rect.y + 20, 10, 5)
                G_bullets.append(bullet2)
                bullet_fire_sound.play()
        if event.type == blue_bullet_hit:
            G_health = G_health - 1
            bullet_hit_sound.play()
        if event.type == green_bullet_hit:
            B_health = B_health - 1
            bullet_hit_sound.play()
    if B_health <= 0:
        winner = "green submarine wins"
        text_colour = "yellow"
    if G_health <= 0:
        winner = "blue submarine wins"
        text_colour = "red"
    if winner != "":
        wintext = H_font.render(winner, 1, text_colour) 
        screen.blit(wintext, (500, 400)) 
        pygame.display.update()
        pygame.time.delay(6000) 
        break    
    key_press = pygame.key.get_pressed()
    move_bullets(G_bullets, B_bullets, G_rect, B_rect)

    move_g(key_press, G_rect)
    move_b(key_press, B_rect)
    draw_window(G_rect, B_rect, B_bullets, G_bullets)
    pygame.display.update()