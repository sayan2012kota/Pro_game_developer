import pygame 
pygame.init()

screen = pygame.display.set_mode((800, 600))

temple_run = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/temple_run.png")
ludo = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/ludo.png")
candy_crush = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/candy_crush.jpg")
subway_surfers = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/subway_surfers.png")

screen.fill("white")

screen.blit(temple_run, (200, 100))
screen.blit(ludo, (200, 200))
screen.blit(candy_crush, (200, 300))
screen.blit(subway_surfers, (200, 400))
font = pygame.font.SysFont("Calibra", 36)
candy = font.render("candy crush", True, "Black")
temple = font.render("temple run", True, "Black")
subway = font.render("subway surfers", True, "Black")
lud = font.render("ludo", True, "Black")
screen.blit(candy, (500, 100))
screen.blit(temple, (500, 200))
screen.blit(subway, (500, 300))
screen.blit(lud, (500, 400))
pygame.display.update()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "Red", mouse_pos, 30, 50)
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_pos2 = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "Red", mouse_pos2, 30, 50)
        pygame.draw.line(screen, "Red", mouse_pos, mouse_pos2, 5)
    pygame.display.update()