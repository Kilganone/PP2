import pygame

class Ball:
    def __init__(self, screen_width: int, screen_height: int):
        self.radius = 25
        self.color = (255, 0, 0)
        self.step = 20
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = screen_width // 2
        self.y = screen_height // 2

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, direction: int):
        new_x, new_y = self.x, self.y

        if direction == pygame.K_LEFT:
            new_x -= self.step
        elif direction == pygame.K_RIGHT:
            new_x += self.step
        elif direction == pygame.K_UP:
            new_y -= self.step
        elif direction == pygame.K_DOWN:
            new_y += self.step
        else:
            return

        if self.radius <= new_x <= self.screen_width - self.radius:
            self.x = new_x
        if self.radius <= new_y <= self.screen_height - self.radius:
            self.y = new_y