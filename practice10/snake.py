import pygame
import random
import time

pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
INITIAL_SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0
    
    snake_List = []
    Length_of_snake = 1
    score = 0
    level = 1
    speed = INITIAL_SPEED

    
    def generate_food():
        while True:
            fx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            fy = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            if [fx, fy] not in snake_List: 
                return fx, fy

    foodx, foody = generate_food()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
        
        pygame.draw.rect(screen, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
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

        
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            Length_of_snake += 1
            score += 1
            
            if score % 3 == 0: 
                level += 1
                speed += 2

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()
