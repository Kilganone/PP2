import pygame
from tools import flood_fill, get_shape_points, save_canvas

# --- CONFIGURATION & COLORS ---
WIDTH, HEIGHT = 900, 750
WHITE, BLACK, GRAY = (255, 255, 255), (0, 0, 0), (200, 200, 200)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
YELLOW, BROWN = (255, 255, 0), (139, 69, 19)
ORANGE, PINK = (255, 165, 0), (255, 192, 203)
PURPLE, CYAN = (128, 0, 128), (0, 255, 255)
DARK_GRAY = (100, 100, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Pro - Ultra Palette")

# --- APPLICATION STATE ---
# Create a separate Surface for the drawing area to prevent UI overlap
canvas = pygame.Surface((WIDTH, HEIGHT - 150))
canvas.fill(WHITE)

current_color = BLACK
current_tool = "brush"
current_thickness = 2
is_filled = False    # Toggle for shapes: True = solid, False = outline
drawing = False      # Track if the mouse is currently held down for drawing
start_pos = None     # Starting coordinate for shapes
last_pos = None      # Previous coordinate for smooth brush strokes
is_typing = False    # Text input mode flag
text_input, text_pos = "", None

# --- UI LAYOUT SETUP ---
# Navigation/Tool buttons (Top row)
tools_list = [
    {"name": "brush", "rect": pygame.Rect(10, 10, 80, 30)},
    {"name": "line", "rect": pygame.Rect(100, 10, 80, 30)},
    {"name": "rect", "rect": pygame.Rect(190, 10, 80, 30)},
    {"name": "circle", "rect": pygame.Rect(280, 10, 80, 30)},
    {"name": "square", "rect": pygame.Rect(370, 10, 80, 30)},
    {"name": "rtriangle", "rect": pygame.Rect(460, 10, 95, 30)},
    {"name": "etriangle", "rect": pygame.Rect(565, 10, 95, 30)},
    {"name": "rhombus", "rect": pygame.Rect(670, 10, 80, 30)},
    {"name": "text", "rect": pygame.Rect(760, 10, 80, 30)},
]

# Action/Utility buttons
action_btns = [
    {"name": "bucket", "rect": pygame.Rect(600, 50, 80, 30)},
    {"name": "eraser", "rect": pygame.Rect(690, 50, 80, 30)},
    {"name": "clear", "rect": pygame.Rect(780, 50, 80, 30)},
]

# Stroke thickness selectors
size_btns = [
    {"size": 2, "name": "Small (1)", "rect": pygame.Rect(300, 50, 85, 30)},
    {"size": 5, "name": "Med (2)", "rect": pygame.Rect(395, 50, 85, 30)},
    {"size": 10, "name": "Large (3)", "rect": pygame.Rect(490, 50, 85, 30)},
]

# Color palette grid (3 rows x 4 columns)
colors = [
    {"color": RED, "rect": pygame.Rect(10, 50, 30, 30)},
    {"color": GREEN, "rect": pygame.Rect(50, 50, 30, 30)},
    {"color": BLUE, "rect": pygame.Rect(90, 50, 30, 30)},
    {"color": BLACK, "rect": pygame.Rect(130, 50, 30, 30)},
    {"color": WHITE, "rect": pygame.Rect(10, 85, 30, 30)},
    {"color": YELLOW, "rect": pygame.Rect(50, 85, 30, 30)},
    {"color": BROWN, "rect": pygame.Rect(90, 85, 30, 30)},
    {"color": ORANGE, "rect": pygame.Rect(130, 85, 30, 30)},
    {"color": PINK, "rect": pygame.Rect(10, 120, 30, 30)},
    {"color": PURPLE, "rect": pygame.Rect(50, 120, 30, 30)},
    {"color": CYAN, "rect": pygame.Rect(90, 120, 30, 30)},
    {"color": DARK_GRAY, "rect": pygame.Rect(130, 120, 30, 30)},
]

def draw_ui():
    """Renders the top control panel and all UI elements."""
    pygame.draw.rect(screen, (220, 220, 220), (0, 0, WIDTH, 150))
    font = pygame.font.SysFont(None, 18)
    
    # Draw Tool and Action buttons
    for btn_group in [tools_list, action_btns]:
        for b in btn_group:
            # Highlight active tool
            bg = WHITE if current_tool == b["name"] else GRAY
            pygame.draw.rect(screen, bg, b["rect"])
            pygame.draw.rect(screen, BLACK, b["rect"], 1)
            screen.blit(font.render(b["name"].upper(), True, BLACK), (b["rect"].x + 5, b["rect"].y + 7))
    
    # Draw Thickness buttons
    for b in size_btns:
        bg = (180, 255, 180) if current_thickness == b["size"] else WHITE
        pygame.draw.rect(screen, bg, b["rect"])
        pygame.draw.rect(screen, BLACK, b["rect"], 1)
        screen.blit(font.render(b["name"], True, BLACK), (b["rect"].x + 5, b["rect"].y + 7))
        
    # Draw Color palette
    for c in colors:
        pygame.draw.rect(screen, c["color"], c["rect"])
        # Add thick border to currently selected color
        border_weight = 3 if current_color == c["color"] else 1
        pygame.draw.rect(screen, BLACK if current_color == c["color"] else GRAY, c["rect"], border_weight)

    # Draw Auto-fill toggle button
    af_rect = pygame.Rect(180, 50, 100, 30)
    pygame.draw.rect(screen, GREEN if is_filled else GRAY, af_rect)
    pygame.draw.rect(screen, BLACK, af_rect, 1)
    screen.blit(font.render("AUTO-FILL", True, BLACK), (190, 57))
    
    screen.blit(font.render("Ctrl+S: Save", True, BLACK), (WIDTH - 100, 120))

# --- MAIN LOOP ---
running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 150)) # Render the drawing canvas below the UI
    m_pos = pygame.mouse.get_pos()
    
    # In Pygame, width=0 fills the shape. Otherwise, it's the line thickness.
    draw_width = 0 if is_filled else current_thickness

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Keyboard Event Handling
        if event.type == pygame.KEYDOWN:
            # Handle Save Shortcut
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                save_canvas(canvas)
            
            # Handle Text Input Mode
            if is_typing:
                if event.key == pygame.K_RETURN: # Commit text
                    f = pygame.font.SysFont(None, current_thickness * 10)
                    canvas.blit(f.render(text_input, True, current_color), text_pos)
                    is_typing = False; text_input = ""
                elif event.key == pygame.K_ESCAPE: # Cancel
                    is_typing = False; text_input = ""
                elif event.key == pygame.K_BACKSPACE: # Delete last char
                    text_input = text_input[:-1]
                else: # Append typed characters
                    text_input += event.unicode
                continue

        # Mouse Click Event Handling
        if not is_typing and event.type == pygame.MOUSEBUTTONDOWN:
            if m_pos[1] < 150: # Check for UI Interaction
                for t in tools_list:
                    if t["rect"].collidepoint(m_pos): current_tool = t["name"]
                for a in action_btns:
                    if a["rect"].collidepoint(m_pos):
                        if a["name"] == "clear": canvas.fill(WHITE)
                        else: current_tool = a["name"]
                for b in size_btns:
                    if b["rect"].collidepoint(m_pos): current_thickness = b["size"]
                for c in colors:
                    if c["rect"].collidepoint(m_pos): current_color = c["color"]
                if pygame.Rect(180, 50, 100, 30).collidepoint(m_pos): is_filled = not is_filled
            
            else: # Check for Canvas Interaction
                if current_tool == "text":
                    is_typing = True
                    text_pos = (m_pos[0], m_pos[1]-150)
                elif current_tool == "bucket":
                    flood_fill(canvas, m_pos[0], m_pos[1]-150, current_color)
                else: 
                    drawing = True
                    start_pos = (m_pos[0], m_pos[1]-150)
                    last_pos = start_pos

        # Mouse Release: Finalize shape drawing on the canvas
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            end_p = (m_pos[0], m_pos[1]-150)
            if current_tool == "line":
                pygame.draw.line(canvas, current_color, start_pos, end_p, current_thickness)
            elif current_tool == "rect":
                r = pygame.Rect(start_pos, (end_p[0]-start_pos[0], end_p[1]-start_pos[1]))
                r.normalize()
                pygame.draw.rect(canvas, current_color, r, draw_width)
            elif current_tool == "square":
                side = min(abs(end_p[0]-start_pos[0]), abs(end_p[1]-start_pos[1]))
                # Determine orientation based on mouse drag direction
                dx = 1 if end_p[0] > start_pos[0] else -1
                dy = 1 if end_p[1] > start_pos[1] else -1
                r = pygame.Rect(start_pos, (dx * side, dy * side))
                r.normalize()
                pygame.draw.rect(canvas, current_color, r, draw_width)
            elif current_tool == "circle":
                rad = int(((start_pos[0]-end_p[0])**2 + (start_pos[1]-end_p[1])**2)**0.5)
                if rad > 0: pygame.draw.circle(canvas, current_color, start_pos, rad, draw_width)
            elif current_tool in ["rtriangle", "etriangle", "rhombus"]:
                pts = get_shape_points(current_tool, start_pos, end_p)
                if pts: pygame.draw.polygon(canvas, current_color, pts, draw_width)
            
            drawing = False; last_pos = None

    # ACTIVE BRUSH/ERASER LOGIC (Continuous drawing)
    if drawing and m_pos[1] > 150:
        curr_p = (m_pos[0], m_pos[1]-150)
        if last_pos:
            if current_tool == "brush":
                # Draw lines between points to prevent gaps during fast movement
                pygame.draw.line(canvas, current_color, last_pos, curr_p, current_thickness)
                pygame.draw.circle(canvas, current_color, curr_p, current_thickness // 2)
            elif current_tool == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, curr_p, 30)
                pygame.draw.circle(canvas, WHITE, curr_p, 15)
        last_pos = curr_p

    # Draw the UI panel on top of the drawing
    draw_ui()
    
    # Real-time text preview while typing
    if is_typing:
        tf = pygame.font.SysFont(None, current_thickness * 10)
        screen.blit(tf.render(text_input + "|", True, current_color), (text_pos[0], text_pos[1]+150))

    # LIVE PREVIEW (Draws a ghost shape on screen while dragging, before committing to canvas)
    if drawing and m_pos[1] > 150 and current_tool not in ["brush", "eraser"]:
        # Offset start position by 150 because we are drawing directly to 'screen' (0-indexed)
        s_start = (start_pos[0], start_pos[1]+150)
        if current_tool == "line":
            pygame.draw.line(screen, current_color, s_start, m_pos, current_thickness)
        elif current_tool == "rect":
            r = pygame.Rect(s_start, (m_pos[0]-s_start[0], m_pos[1]-s_start[1]))
            r.normalize(); pygame.draw.rect(screen, current_color, r, draw_width)
        elif current_tool == "square":
            side = min(abs(m_pos[0]-s_start[0]), abs(m_pos[1]-s_start[1]))
            dx = 1 if m_pos[0] > s_start[0] else -1
            dy = 1 if m_pos[1] > s_start[1] else -1
            r = pygame.Rect(s_start, (dx * side, dy * side))
            r.normalize(); pygame.draw.rect(screen, current_color, r, draw_width)
        elif current_tool == "circle":
            rad = int(((start_pos[0]-(m_pos[0]))**2 + (start_pos[1]-(m_pos[1]-150))**2)**0.5)
            if rad > 0: pygame.draw.circle(screen, current_color, s_start, rad, draw_width)
        elif current_tool in ["rtriangle", "etriangle", "rhombus"]:
            pts = get_shape_points(current_tool, start_pos, (m_pos[0], m_pos[1]-150))
            s_pts = [(p[0], p[1] + 150) for p in pts] # Apply UI offset to points
            if s_pts: pygame.draw.polygon(screen, current_color, s_pts, draw_width)

    pygame.display.flip()

pygame.quit()