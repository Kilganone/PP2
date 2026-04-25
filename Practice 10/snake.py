import pygame
import random

# --- INITIALIZATION ---
pygame.init()

# Window dimensions and grid size
WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game clock to control frame rate
clock = pygame.time.Clock()

# Color definitions (RGB)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font for UI
font = pygame.font.SysFont("Arial", 24)

# --- GAME SETTINGS ---
snake = [(100, 100)]  # List containing snake segment coordinates
direction = (CELL, 0) # Initial movement direction (Right)

score = 0
level = 1
speed = 10

foods_eaten = 0  # Counter to track level progression


# --- FOOD GENERATION FUNCTION ---
def generate_food():
    """Generates food coordinates that do not overlap with the snake body"""
    while True:
        food = (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))
        if food not in snake:
            return food


food = generate_food()

# --- MAIN GAME LOOP ---
running = True
while running:
    # Set the game speed based on current level
    clock.tick(speed)

    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input for direction changes
        # Prevents the snake from reversing directly into itself
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    # --- SNAKE MOVEMENT ---
    # Calculate new head position based on current direction
    head = (snake[0][0] + direction[0],
            snake[0][1] + direction[1])

    # Add the new head to the front of the snake list
    snake.insert(0, head)

    # --- CHECK: FOOD COLLECTION ---
    if head == food:
        score += 1
        foods_eaten += 1
        food = generate_food() # Create new food if eaten
    else:
        # If no food is eaten, remove the tail to maintain length
        snake.pop()

    # --- CHECK: COLLISIONS ---
    # Wall collision check
    if (head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT):
        running = False

    # Self-collision check (if head hits any other segment)
    if head in snake[1:]:
        running = False

    # --- LEVEL LOGIC ---
    # Every 4 food items, the level increases and speed goes up
    if foods_eaten >= 4:
        level += 1
        speed += 2
        foods_eaten = 0

    # --- RENDERING ---
    screen.fill(BLACK)

    # Draw the snake body
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    # Draw the food
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    # --- UI (Score and Level) ---
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Update the full display Surface to the screen
    pygame.display.flip()

pygame.quit()