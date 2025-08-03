import pygame
pygame.init()
screen = pygame.display.set_mode((900, 300))
pygame.display.set_caption("Circle")


class Circle():
    def __init__(self, colour, dim):
        self.circle_surface = screen
        self.circle_colour = colour
        self.circle_dimension = dim

    def draw_circle(self):
        pygame.draw.circle(self.circle_surface, self.circle_colour, self.circle_dimension, 150, 20)

screen.fill("white")

circle = Circle("red", (200, 150))
circle.draw_circle()

pygame.display.update()

run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False







pygame.quit()