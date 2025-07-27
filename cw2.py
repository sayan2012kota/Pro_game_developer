import pygame
pygame.init()
screen = pygame.display.set_mode((700, 300))
pygame.display.set_caption("Rectangle")

class Rect():
    def __init__(self, colour, dim):
        self.rectangle_surface = screen
        self.rectangle_colour = colour
        self.rectangle_dimension = dim

    def draw_rectangle(self):
        pygame.draw.rect(self.rectangle_surface, self.rectangle_colour, self.rectangle_dimension, 20)

    
screen.fill("white")

rectangle = Rect("blue", (100, 30, 120, 150))
second_rect = Rect("red", (300, 30, 120, 150))
third_rect = Rect("green", (500, 30, 120, 150))

rectangle.draw_rectangle()
second_rect.draw_rectangle()
third_rect.draw_rectangle()

pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            run = False






pygame.quit()

