import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BASE_SPEED = 5
SCORE = 0
COIN_SCORE = 0
SPEED_UP_EVERY = 5

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

COIN_TYPES = [
    {"color": (255, 215, 0),   "value": 1, "size": 20},
    {"color": (192, 192, 192), "value": 3, "size": 25},
    {"color": (205, 127, 50),  "value": 5, "size": 30},
]

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

font_small = pygame.font.SysFont("Verdana", 20)
font = pygame.font.SysFont("Verdana", 60)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = BASE_SPEED

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def increase_speed(self):
        self.speed += 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ctype = None
        self.value = 0
        self.respawn()

    def respawn(self):
        self.ctype = random.choice(COIN_TYPES)
        self.value = self.ctype["value"]
        size = self.ctype["size"]
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.ctype["color"], (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), random.randint(-300, -30))

    def move(self):
        self.rect.move_ip(0, BASE_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()


P1 = Player()
E1 = Enemy()

coins = pygame.sprite.Group()
for _ in range(5):
    c = Coin()
    c.rect.y -= _ * 80
    coins.add(c)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)
for c in coins:
    all_sprites.add(c)

prev_milestone = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    hud = font_small.render(f"Coins: {COIN_SCORE}   Speed: {E1.speed}", True, BLACK)
    DISPLAYSURF.blit(hud, (10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    for coin in pygame.sprite.spritecollide(P1, coins, False):
        COIN_SCORE += coin.value
        coin.respawn()

    milestone = COIN_SCORE // SPEED_UP_EVERY
    if milestone > prev_milestone:
        E1.increase_speed()
        prev_milestone = milestone

    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
