import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

geometry_dash = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/geomatery_dash.png")
block_blast = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/block_blast.png")
pokemon = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/pokemon_logo.jpg")
wordscape = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/wordscape_logo.png")

geometry_dash = pygame.transform.scale(geometry_dash, (80, 80))
block_blast = pygame.transform.scale(block_blast, (80, 80))
pokemon = pygame.transform.scale(pokemon, (80, 80))
wordscape = pygame.transform.scale(wordscape, (80, 80))

screen.fill("white")

screen.blit(geometry_dash, (200, 100))
screen.blit(block_blast, (200, 200))
screen.blit(pokemon, (200, 300))
screen.blit(wordscape, (200, 400))
font = pygame.font.SysFont("Calibra", 36)
pokemo = font.render("pokemon", True, "Black")
geomet = font.render("geometry dash", True, "Black")
wordscap = font.render("wordscape", True, "Black")
block = font.render("block blast", True, "Black")
screen.blit(pokemo, (500, 100))
screen.blit(geomet, (500, 200))
screen.blit(wordscap, (500, 300))
screen.blit(block, (500, 400))
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