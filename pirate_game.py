import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1100, 900))

pirate_bg = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/pirate_bg.png")
pirate_bg = pygame.transform.scale(pirate_bg, (1100, 900))

class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/pirate_image.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

sprites = pygame.sprite.Group()
pirate = Pirate()
sprites.add(pirate)

class Points(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load(x)
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()

second_sprites = pygame.sprite.Group()
point_gainers = ["C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/treasure.png",
            "C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/coin.jpg",
            "C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/rum.png"]

for i in range(50):
    pencil = Points(random.choice(point_gainers))
    pencil.rect.x = random.randint(50, 1000)
    pencil.rect.y = random.randint(50, 850)
    second_sprites.add(pencil)
    sprites.add(pencil)

class Losing(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()   
        self.image = pygame.image.load(y)
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()   
        

point_losers = ["C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/evil_fish.png",
                "C:/Users/pooja/Desktop/pro_game_development/Game_developer2/lesson_3/enemy_pirate.png"]

third_sprites = pygame.sprite.Group()
for r in range(20):
    plastic_bag = Losing(random.choice(point_losers))
    plastic_bag.rect.x = random.randint(50, 1000)
    plastic_bag.rect.y = random.randint(50, 850)
    third_sprites.add(plastic_bag)
    sprites.add(plastic_bag)
store_score = 0

def draw_window():
    screen.blit(pirate_bg, (0,0))

S_font = pygame.font.SysFont("Calibra", 30)
score_text = S_font.render("score:"+ str(store_score), True, "black")




# The items that give points are(+1 points):
#coins
#treasure
#bottle of rum
# The items that lose points are(-3 points):
#evil fish
#enemy pirates(mainly look red)


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_UP]:
        if pirate.rect.y > 0:
            pirate.rect.y = pirate.rect.y - 2
    if key_press[pygame.K_DOWN]:
        if pirate.rect.y < 850:
            pirate.rect.y = pirate.rect.y + 2
    if key_press[pygame.K_LEFT]:
        if pirate.rect.x > 0:
            pirate.rect.x = pirate.rect.x - 2
    if key_press[pygame.K_RIGHT]:
        if pirate.rect.x < 1050:
            pirate.rect.x = pirate.rect.x + 2  
    gaining_list = pygame.sprite.spritecollide(pirate, second_sprites, True)
    losing_list = pygame.sprite.spritecollide(pirate, third_sprites, True)
    for variable in gaining_list:
        store_score = store_score + 1
        score_text = S_font.render("score:"+ str(store_score), True, "black")
    for item in losing_list:
        store_score = store_score - 3
        score_text = S_font.render("score:"+ str(store_score), True, "black")
    draw_window()
    screen.blit(score_text, (50, 50))
    sprites.draw(screen)
    pygame.display.update()
    