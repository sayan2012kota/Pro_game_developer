import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
screen.fill("white")

pygame.display.update()
run = True

class Shapes():
    def __init__(self,x, y, radius, width, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.colour = colour
        self.surface = screen

    def draw_circle(self):
        pygame.draw.circle(self.surface, self.colour, (self.x, self.y), self.radius,  self.width)



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False













