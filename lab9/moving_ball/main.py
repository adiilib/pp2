import pygame
import sys
from ball import Ball

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 16)

    ball = Ball(WIDTH // 2, HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move(0, -ball.step, WIDTH, HEIGHT)
                elif event.key == pygame.K_DOWN:
                    ball.move(0, ball.step, WIDTH, HEIGHT)
                elif event.key == pygame.K_LEFT:
                    ball.move(-ball.step, 0, WIDTH, HEIGHT)
                elif event.key == pygame.K_RIGHT:
                    ball.move(ball.step, 0, WIDTH, HEIGHT)

        screen.fill(WHITE)

        hint = font.render("Arrow keys to move", True, GRAY)
        screen.blit(hint, (10, 10))

        pos = font.render(f"x={ball.x}  y={ball.y}", True, GRAY)
        screen.blit(pos, (10, 30))

        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)


main()
