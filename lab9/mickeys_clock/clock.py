import pygame
import math
import datetime
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (210, 40, 40)


class MickeyClock:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        img_path = os.path.join(os.path.dirname(__file__), "..", "images", "mickeyclock.jpeg")
        raw = pygame.image.load(img_path)
        self.bg = pygame.transform.scale(raw, (width, height))

        self.cx = width // 2
        self.cy = int(height * 0.50)

    def draw_hand(self, angle_deg, length, color, width, glove_r):
        angle_rad = math.radians(angle_deg - 90)
        ex = self.cx + length * math.cos(angle_rad)
        ey = self.cy + length * math.sin(angle_rad)
        pygame.draw.line(self.screen, BLACK, (self.cx, self.cy), (int(ex), int(ey)), width + 3)
        pygame.draw.line(self.screen, color, (self.cx, self.cy), (int(ex), int(ey)), width)
        pygame.draw.circle(self.screen, WHITE, (int(ex), int(ey)), glove_r)
        pygame.draw.circle(self.screen, BLACK, (int(ex), int(ey)), glove_r, 2)

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        now = datetime.datetime.now()
        min_angle = now.minute * 6
        sec_angle = now.second * 6

        self.draw_hand(min_angle, int(self.width * 0.30), BLACK, 7, 22)
        self.draw_hand(sec_angle, int(self.width * 0.30), RED, 4, 16)

        pygame.draw.circle(self.screen, BLACK, (self.cx, self.cy), 10)
