import pygame

RED = (220, 50, 50)
BLACK = (0, 0, 0)


class Ball:
    def __init__(self, x, y, radius=25):
        self.x = x
        self.y = y
        self.radius = radius
        self.step = 20

    def move(self, dx, dy, screen_w, screen_h):
        new_x = self.x + dx
        new_y = self.y + dy
        if self.radius <= new_x <= screen_w - self.radius:
            self.x = new_x
        if self.radius <= new_y <= screen_h - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius + 2)
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)
