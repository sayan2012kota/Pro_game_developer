import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
screen.fill("white")

pygame.display.update()
run = True

class Shapes():
    def __init__(self,x, y, length, height, width, colour):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.colour = colour
        self.surface = screen

    def draw_rect(self):
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.length, self.height), self.width)

    def increase_size(self):
        self.length = self.length + 10
        self.height = self.height + 10
        self.draw_rect()

rect = Shapes(750, 500, 50, 50, 3, "red")
rect_2 = Shapes(250, 500, 100, 70, 5, "green")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rect.draw_rect()
            rect_2.draw_rect()
            pygame.display.update()
        elif event.type ==  pygame.MOUSEBUTTONUP:
            rect.increase_size()
            rect_2.increase_size()
            pygame.display.update()













