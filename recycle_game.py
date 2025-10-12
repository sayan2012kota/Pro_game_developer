import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1100, 900))
recycle_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/recycle background.png")

recycle_bg = pygame.transform.scale(recycle_bg,  (1100, 900))

pygame.display.set_caption("Recycle game!")

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/bin.png")
        self.image = pygame.transform.scale(self.image, (50, 90))
        self.rect = self.image.get_rect()

sprites = pygame.sprite.Group()
bin = Bin()
sprites.add(bin)
    
def draw_window():
    screen.blit(recycle_bg, (0,0))









while True:
    for b in pygame.event.get():
        if b.type == pygame.QUIT:
            pygame.quit()
    sprites.draw(screen)
    pygame.display.update()
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_UP]:
        if bin.rect.y > 0:
            bin.rect.y = bin.rect.y - 1
    if key_press[pygame.K_DOWN]:
        if bin.rect.y < 1100:
            bin.rect.y = bin.rect.y + 1
    draw_window()
