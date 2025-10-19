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

class Recyclables(pygame.sprite.Sprite):
    def __init__(self, x, ):
        super().__init__()
        self.image = pygame.image.load(x)
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        
second_sprites = pygame.sprite.Group()
recycle = ["C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/item1.png",
            "C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/pencil.png",
            "C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/Wood_box.png"]

for i in range(50):
    pencil = Recyclables(random.choice(recycle))
    pencil.rect.x = random.randint(50, 1000)
    pencil.rect.y = random.randint(50, 850)
    second_sprites.add(pencil)
    sprites.add(pencil)
            

class Unrecyclables(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_2/plastic bag.png")
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()

third_sprites = pygame.sprite.Group()
for r in range(20):
    plastic_bag = Unrecyclables()
    plastic_bag.rect.x = random.randint(50, 1000)
    plastic_bag.rect.y = random.randint(50, 850)
    third_sprites.add(plastic_bag)
    sprites.add(plastic_bag)
store_score = 0

def draw_window():
    screen.blit(recycle_bg, (0,0))

S_font = pygame.font.SysFont("Calibra", 30)
score_text = S_font.render("score:"+ str(store_score), True, "black")










while True:
    for b in pygame.event.get():
        if b.type == pygame.QUIT:
            pygame.quit()
    sprites.draw(screen)
    pygame.display.update()
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_UP]:
        if bin.rect.y > 0:
            bin.rect.y = bin.rect.y - 2
    if key_press[pygame.K_DOWN]:
        if bin.rect.y < 850:
            bin.rect.y = bin.rect.y + 2
    if key_press[pygame.K_LEFT]:
        if bin.rect.x > 0:
            bin.rect.x = bin.rect.x - 2
    if key_press[pygame.K_RIGHT]:
        if bin.rect.x < 1050:
            bin.rect.x = bin.rect.x + 2  
    recyclable_list = pygame.sprite.spritecollide(bin, second_sprites, True)
    unrecyclable_list = pygame.sprite.spritecollide(bin, third_sprites, True)
    for variable in recyclable_list:
        store_score = store_score + 1
        score_text = S_font.render("score:"+ str(store_score), True, "black")
    for item in unrecyclable_list:
        store_score = store_score - 5
        score_text = S_font.render("score:"+ str(store_score), True, "black")
    screen.blit(score_text, (50, 50))
    pygame.display.update()
    draw_window()
    

