import pygame
pygame.init()
screen = pygame.display.set_mode((900, 300))
pygame.display.set_caption("Circle")

run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#class Circle()







pygame.quit()