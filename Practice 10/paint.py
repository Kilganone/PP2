import pygame

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minimalist Paint - Filled Shapes")

# --- STATE VARIABLES ---
# Separate surface for the drawing area to keep UI and artwork separate
canvas = pygame.Surface((WIDTH, HEIGHT - 100))
canvas.fill(WHITE)

current_color = BLACK
current_tool = "brush"  # Options: brush, rect, circle, eraser
drawing = False
start_pos = None

# Tool button definitions
tools = [
    {"name": "brush", "rect": pygame.Rect(10, 10, 80, 30)},
    {"name": "rect", "rect": pygame.Rect(100, 10, 80, 30)},
    {"name": "circle", "rect": pygame.Rect(190, 10, 80, 30)},
    {"name": "eraser", "rect": pygame.Rect(280, 10, 80, 30)},
]

# Color palette buttons
colors = [
    {"name": "red", "rect": pygame.Rect(400, 10, 30, 30), "color": RED},
    {"name": "green", "rect": pygame.Rect(440, 10, 30, 30), "color": GREEN},
    {"name": "blue", "rect": pygame.Rect(480, 10, 30, 30), "color": BLUE},
    {"name": "black", "rect": pygame.Rect(520, 10, 30, 30), "color": BLACK},
]

def draw_ui():
    """Renders the top toolbar, tool buttons, and color selectors"""
    # Draw background for the toolbar
    pygame.draw.rect(screen, (230, 230, 230), (0, 0, WIDTH, 100))
    font = pygame.font.SysFont(None, 22)
    
    # Draw tool buttons
    for t in tools:
        is_active = current_tool == t["name"]
        pygame.draw.rect(screen, WHITE if is_active else GRAY, t["rect"])
        pygame.draw.rect(screen, BLACK, t["rect"], 2 if is_active else 1)
        text = font.render(t["name"].upper(), True, BLACK)
        screen.blit(text, (t["rect"].x + 10, t["rect"].y + 7))

    # Draw color buttons
    for c in colors:
        is_active = current_color == c["color"] and current_tool != "eraser"
        pygame.draw.rect(screen, c["color"], c["rect"])
        pygame.draw.rect(screen, BLACK, c["rect"], 3 if is_active else 1)

# --- MAIN LOOP ---
running = True
while running:
    # Clear screen and blit the persistent canvas below the UI
    screen.fill(WHITE)
    screen.blit(canvas, (0, 100)) 
    
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[1] < 100: # Toolbar interaction
                for t in tools:
                    if t["rect"].collidepoint(mouse_pos):
                        current_tool = t["name"]
                for c in colors:
                    if c["rect"].collidepoint(mouse_pos):
                        current_color = c["color"]
                        # Switching to a color automatically selects brush if eraser was active
                        if current_tool == "eraser": current_tool = "brush"
            else: # Canvas interaction
                drawing = True
                # Offset coordinate to match canvas local space
                start_pos = (mouse_pos[0], mouse_pos[1] - 100)

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = (mouse_pos[0], mouse_pos[1] - 100)
                
                # Commit shape to the persistent canvas surface
                if current_tool == "rect":
                    r = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                    r.normalize() # Ensure width/height are positive
                    pygame.draw.rect(canvas, current_color, r, 0) # 0 = filled
                elif current_tool == "circle":
                    # Calculate Euclidean distance for radius
                    radius = int(((start_pos[0]-end_pos[0])**2 + (start_pos[1]-end_pos[1])**2)**0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 0)
                
                drawing = False

    # Real-time drawing for Brush and Eraser (continuous application)
    if drawing and mouse_pos[1] > 100:
        curr_canvas_pos = (mouse_pos[0], mouse_pos[1] - 100)
        if current_tool == "brush":
            pygame.draw.circle(canvas, current_color, curr_canvas_pos, 5)
        elif current_tool == "eraser":
            pygame.draw.circle(canvas, WHITE, curr_canvas_pos, 20)

    draw_ui()

    # Shape Preview: Renders temporary shape while mouse is dragging
    if drawing and mouse_pos[1] > 100:
        curr_screen_pos = mouse_pos
        start_screen_pos = (start_pos[0], start_pos[1] + 100) # Convert back to screen space
        
        if current_tool == "rect":
            r = pygame.Rect(start_screen_pos, (curr_screen_pos[0]-start_screen_pos[0], curr_screen_pos[1]-start_screen_pos[1]))
            pygame.draw.rect(screen, current_color, r, 0)
        elif current_tool == "circle":
            radius = int(((start_screen_pos[0]-curr_screen_pos[0])**2 + (start_screen_pos[1]-curr_screen_pos[1])**2)**0.5)
            pygame.draw.circle(screen, current_color, start_screen_pos, radius, 0)

    pygame.display.flip()

pygame.quit()