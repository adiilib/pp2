import pygame
import sys
from player import MusicPlayer

WIDTH, HEIGHT = 520, 340
BG = (20, 20, 35)
ACCENT = (100, 200, 255)
WHITE = (255, 255, 255)
GRAY = (140, 140, 160)
GREEN = (80, 200, 100)
RED = (220, 70, 70)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()

    player = MusicPlayer("music")

    title_font = pygame.font.SysFont("Arial", 26, bold=True)
    track_font = pygame.font.SysFont("Arial", 20)
    info_font = pygame.font.SysFont("Arial", 16)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next()
                elif event.key == pygame.K_b:
                    player.prev()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(BG)

        title = title_font.render("Music Player", True, ACCENT)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

        track_label = track_font.render(player.current_name(), True, WHITE)
        screen.blit(track_label, (WIDTH // 2 - track_label.get_width() // 2, 100))

        if player.tracks:
            pos_text = f"Track {player.index + 1} / {len(player.tracks)}"
            pos_label = info_font.render(pos_text, True, GRAY)
            screen.blit(pos_label, (WIDTH // 2 - pos_label.get_width() // 2, 135))

        status_color = GREEN if player.playing else RED
        status = info_font.render(player.status(), True, status_color)
        screen.blit(status, (WIDTH // 2 - status.get_width() // 2, 170))

        pygame.draw.rect(screen, (40, 40, 60), (30, 210, WIDTH - 60, 90), border_radius=10)

        controls = [
            ("[P] Play", GREEN),
            ("[S] Stop", RED),
            ("[N] Next", ACCENT),
            ("[B] Prev", ACCENT),
            ("[Q] Quit", GRAY),
        ]
        x = 50
        for text, color in controls:
            lbl = info_font.render(text, True, color)
            screen.blit(lbl, (x, 245))
            x += (WIDTH - 80) // len(controls)

        pygame.display.flip()
        clock.tick(30)


main()
