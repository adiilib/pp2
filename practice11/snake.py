import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
INITIAL_SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

FOOD_TYPES = [
    {"color": (220, 50,  50),  "value": 1, "lifetime": 8000},
    {"color": (160, 0,  210),  "value": 3, "lifetime": 5000},
    {"color": (255, 165,  0),  "value": 5, "lifetime": 3000},
]


class Food:
    def __init__(self, snake_list):
        self.x = 0
        self.y = 0
        self.value = 1
        self.color = (255, 0, 0)
        self.lifetime = 8000
        self.spawn_time = 0
        self.respawn(snake_list)

    def respawn(self, snake_list):
        ftype = random.choice(FOOD_TYPES)
        self.value = ftype["value"]
        self.color = ftype["color"]
        self.lifetime = ftype["lifetime"]
        self.spawn_time = pygame.time.get_ticks()
        while True:
            self.x = random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE
            self.y = random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
            if [self.x, self.y] not in snake_list:
                break

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.lifetime

    def draw(self, surface):
        elapsed = pygame.time.get_ticks() - self.spawn_time
        ratio = 1 - elapsed / self.lifetime
        if ratio < 0.3 and (pygame.time.get_ticks() // 200) % 2 == 0:
            return
        pygame.draw.rect(surface, self.color, [self.x, self.y, BLOCK_SIZE, BLOCK_SIZE])
        size_label = pygame.font.SysFont("bahnschrift", 12).render(str(self.value), True, (255, 255, 255))
        surface.blit(size_label, (self.x + 4, self.y + 4))


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def gameLoop():
    game_over = False
    x1, y1 = WIDTH // 2, HEIGHT // 2
    x1_change, y1_change = 0, 0

    snake_List = []
    Length_of_snake = 1
    score = 0
    level = 1
    speed = INITIAL_SPEED

    foods = [Food([]) for _ in range(3)]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change, y1_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change, y1_change = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change, x1_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change, x1_change = BLOCK_SIZE, 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        for food in foods:
            if food.is_expired():
                food.respawn(snake_List)
            food.draw(screen)

        snake_head = [x1, y1]
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_over = True

        for segment in snake_List:
            pygame.draw.rect(screen, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        score_txt = font_style.render(f"Score: {score}  Level: {level}", True, YELLOW)
        screen.blit(score_txt, [10, 10])

        pygame.display.update()

        for food in foods:
            if x1 == food.x and y1 == food.y:
                score += food.value
                Length_of_snake += food.value
                food.respawn(snake_List)
                if score % 5 == 0:
                    level += 1
                    speed += 2

        clock.tick(speed)

    pygame.quit()
    quit()


gameLoop()
