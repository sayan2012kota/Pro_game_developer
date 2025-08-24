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

    def increase_size(self):
        self.radius = self.radius + 10
        self.draw_circle()

circle = Shapes(500, 500, 50, 40, "red")


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            circle.draw_circle()
            pygame.display.update()
        elif event.type ==  pygame.MOUSEBUTTONUP:
            circle.increase_size()
            pygame.display.update()













