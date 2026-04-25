import pygame, sys
from pygame.locals import *
import random, time

# --- INITIALIZATION ---
pygame.init()

# Frame rate controller
FPS = 60
FramePerSec = pygame.time.Clock()

# --- COLORS ---
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- GAME SETTINGS ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0 

# --- FONTS ---
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# --- ASSETS ---
background = pygame.image.load("AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# =========================
# ENEMY CLASS
# =========================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        # Start at random X position above the screen
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # Reset to top if it passes the bottom and increment score
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# =========================
# PLAYER CLASS
# =========================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Keep player within screen boundaries while moving
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# =========================
# COIN CLASS
# =========================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Resize coin image to fit gameplay
        original_image = pygame.image.load("coin.png")
        self.image = pygame.transform.smoothscale(original_image, (40, 40))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        """Respawn coin at random position that doesn't overlap enemy"""
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            # Check coin and enemy collision
            if not self.rect.colliderect(E1.rect):
                break

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

# --- INSTANTIATION ---
P1 = Player()
E1 = Enemy()
C1 = Coin()  # Создаём монету ПОСЛЕ врага, чтобы E1 был определён в reset()

# --- SPRITE GROUPS ---
# Groups allow for bulk updates and easy collision detection
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# --- CUSTOM EVENTS ---
# Trigger speed increase every 1000ms (1 second)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# =========================
# MAIN GAME LOOP
# =========================
while True:

    # Event Handling
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Rendering Background
    DISPLAYSURF.blit(background, (0, 0))

    # Rendering UI Text
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (280, 10))

    # Update and Draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Collision Detection: Player vs Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        C1.reset()

    # Collision Detection: Player vs Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        # Game Over Screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        # Clean up resources before exit
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update display and maintain constant frame rate
    pygame.display.update()
    FramePerSec.tick(FPS)