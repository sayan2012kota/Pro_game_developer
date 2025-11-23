import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 1000))

bday_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/birthday_bg1.jpg")
cake = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/cake.png")
gift = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/gift.png")

bday_bg = pygame.transform.scale(bday_bg, (1000, 1000))
cake = pygame.transform.scale(cake, (1000, 1000))
gift = pygame.transform.scale(gift, (1000,  1000))

message_font = pygame.font.SysFont("Calibra", 100)
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    font = message_font.render("Happy Birthday!", True, "black")
    screen.blit(bday_bg, (0,0))
    screen.blit(font, (100, 400))
    pygame.display.update()
    time.sleep(5)
    screen.blit(cake, (0,0))
    font2 = message_font.render("I hope you enjoy your day :)", True, "black")
    screen.blit(font2, (50, 100))
    pygame.display.update()
    time.sleep(5)
    screen.blit(gift, (0,0))
    font3 = message_font.render("Here are your gifts!", True, "black")
    screen.blit(font3, (100, 100))
    pygame.display.update()
    time.sleep(5)
    
    