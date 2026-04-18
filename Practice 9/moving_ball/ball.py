import pygame

class Ball:
    def __init__(self, width, height):
        self.x = width // 2
        self.y = height // 2

        self.radius = 25
        self.color = (255, 0, 0)
        self.speed = 5

        self.width = width
        self.height = height

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # границы экрана
        self.x = max(self.radius, min(self.x, self.width - self.radius))
        self.y = max(self.radius, min(self.y, self.height - self.radius))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)