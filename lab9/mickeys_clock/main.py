import pygame
import sys
import datetime
from clock import MickeyClock

WIDTH, HEIGHT = 600, 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    tick = pygame.time.Clock()
    mickey = MickeyClock(screen, WIDTH, HEIGHT)
    font = pygame.font.SysFont("Arial", 28, bold=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mickey.draw()

        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M:%S")
        label = font.render(time_str, True, (255, 255, 255))
        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT - 35))

        pygame.display.flip()
        tick.tick(10)


main()
