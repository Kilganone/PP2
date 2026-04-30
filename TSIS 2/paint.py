import pygame
from tools import flood_fill, get_shape_points, save_canvas

# --- CONFIG ---
WIDTH, HEIGHT = 900, 750
WHITE, BLACK, GRAY = (255, 255, 255), (0, 0, 0), (200, 200, 200)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
YELLOW, BROWN = (255, 255, 0), (139, 69, 19)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Pro 2026")

# --- STATE ---
canvas = pygame.Surface((WIDTH, HEIGHT - 150))
canvas.fill(WHITE)
current_color = BLACK
current_tool = "brush"
current_thickness = 2
is_filled = False 
drawing = False
start_pos = None
last_pos = None # Для плавных линий[cite: 1]
text_input, text_pos, is_typing = "", None, False

# UI Setup
# --- ОБНОВЛЕННЫЙ UI SETUP ---
tools_list = [
    # Первый ряд: Фигуры и Рисование
    {"name": "brush", "rect": pygame.Rect(10, 10, 80, 30)},
    {"name": "line", "rect": pygame.Rect(100, 10, 80, 30)},
    {"name": "rect", "rect": pygame.Rect(190, 10, 80, 30)},
    {"name": "circle", "rect": pygame.Rect(280, 10, 80, 30)},
    {"name": "square", "rect": pygame.Rect(370, 10, 80, 30)},
    {"name": "rtriangle", "rect": pygame.Rect(460, 10, 95, 30)},
    {"name": "etriangle", "rect": pygame.Rect(565, 10, 95, 30)},
    {"name": "rhombus", "rect": pygame.Rect(670, 10, 80, 30)},
    {"name": "text", "rect": pygame.Rect(760, 10, 80, 30)},
    
    # Третий ряд: Утилиты (поднял повыше, чтобы не было нахлеста)
    {"name": "bucket", "rect": pygame.Rect(300, 90, 80, 30)},
    {"name": "eraser", "rect": pygame.Rect(390, 90, 80, 30)},
    {"name": "clear", "rect": pygame.Rect(480, 90, 80, 30)},
]

size_btns = [
    {"size": 2, "name": "Small (1)", "rect": pygame.Rect(300, 50, 80, 30)},
    {"size": 5, "name": "Med (2)", "rect": pygame.Rect(390, 50, 80, 30)},
    {"size": 10, "name": "Large (3)", "rect": pygame.Rect(480, 50, 80, 30)},
]

colors = [
    # Ряд 1 цветов
    {"color": RED, "rect": pygame.Rect(10, 50, 30, 30)},
    {"color": GREEN, "rect": pygame.Rect(50, 50, 30, 30)},
    {"color": BLUE, "rect": pygame.Rect(90, 50, 30, 30)},
    {"color": BLACK, "rect": pygame.Rect(130, 50, 30, 30)},
    # Ряд 2 цветов
    {"color": WHITE, "rect": pygame.Rect(10, 90, 30, 30)},
    {"color": YELLOW, "rect": pygame.Rect(50, 90, 30, 30)},
    {"color": BROWN, "rect": pygame.Rect(90, 90, 30, 30)},
]

# Кнопка Auto-Fill отдельно
autofill_rect = pygame.Rect(180, 50, 100, 30)
def draw_ui():
    pygame.draw.rect(screen, (230, 230, 230), (0, 0, WIDTH, 150))
    font = pygame.font.SysFont(None, 18)
    for t in tools_list:
        pygame.draw.rect(screen, WHITE if current_tool == t["name"] else GRAY, t["rect"])
        pygame.draw.rect(screen, BLACK, t["rect"], 1)
        screen.blit(font.render(t["name"].upper(), True, BLACK), (t["rect"].x + 5, t["rect"].y + 7))
    for b in size_btns:
        pygame.draw.rect(screen, (180, 255, 180) if current_thickness == b["size"] else WHITE, b["rect"])
        pygame.draw.rect(screen, BLACK, b["rect"], 1)
        screen.blit(font.render(b["name"], True, BLACK), (b["rect"].x + 5, b["rect"].y + 7))
    for c in colors:
        pygame.draw.rect(screen, c["color"], c["rect"])
        if current_color == c["color"]: pygame.draw.rect(screen, BLACK, c["rect"], 3)
    pygame.draw.rect(screen, GREEN if is_filled else GRAY, (180, 50, 100, 30))
    screen.blit(font.render("AUTO-FILL", True, BLACK), (190, 57))
    screen.blit(font.render("Ctrl+S: Save", True, BLACK), (WIDTH - 120, 120))

# --- MAIN LOOP ---
running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 150))
    m_pos = pygame.mouse.get_pos()
    thick = 0 if is_filled else current_thickness

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                save_canvas(canvas)
            if is_typing:
                if event.key == pygame.K_RETURN:
                    f = pygame.font.SysFont(None, current_thickness * 10)
                    canvas.blit(f.render(text_input, True, current_color), text_pos)
                    is_typing = False; text_input = ""
                elif event.key == pygame.K_ESCAPE: is_typing = False; text_input = ""
                elif event.key == pygame.K_BACKSPACE: text_input = text_input[:-1]
                else: text_input += event.unicode
                continue

        if not is_typing and event.type == pygame.MOUSEBUTTONDOWN:
            if m_pos[1] < 150:
                for t in tools_list:
                    if t["rect"].collidepoint(m_pos):
                        if t["name"] == "clear": canvas.fill(WHITE) # Кнопка очистки[cite: 1]
                        else: current_tool = t["name"]
                for b in size_btns:
                    if b["rect"].collidepoint(m_pos): current_thickness = b["size"]
                for c in colors:
                    if c["rect"].collidepoint(m_pos): current_color = c["color"]
                if pygame.Rect(180, 50, 100, 30).collidepoint(m_pos): is_filled = not is_filled
            else:
                if current_tool == "text": is_typing = True; text_pos = (m_pos[0], m_pos[1]-150)
                elif current_tool == "bucket": flood_fill(canvas, m_pos[0], m_pos[1]-150, current_color)
                else: 
                    drawing = True
                    start_pos = (m_pos[0], m_pos[1]-150)
                    last_pos = start_pos # Начало плавной линии[cite: 1]

        if event.type == pygame.MOUSEBUTTONUP and drawing:
            end_p = (m_pos[0], m_pos[1]-150)
            if current_tool == "line": pygame.draw.line(canvas, current_color, start_pos, end_p, current_thickness)
            elif current_tool == "rect":
                r = pygame.Rect(start_pos, (end_p[0]-start_pos[0], end_p[1]-start_pos[1]))
                r.normalize(); pygame.draw.rect(canvas, current_color, r, thick)
            elif current_tool == "square":
                s = min(abs(end_p[0]-start_pos[0]), abs(end_p[1]-start_pos[1]))
                r = pygame.Rect(start_pos, ((1 if end_p[0]>start_pos[0] else -1)*s, (1 if end_p[1]>start_pos[1] else -1)*s))
                r.normalize(); pygame.draw.rect(canvas, current_color, r, thick)
            elif current_tool == "circle":
                rad = int(((start_pos[0]-end_p[0])**2 + (start_pos[1]-end_p[1])**2)**0.5)
                if rad > 0: pygame.draw.circle(canvas, current_color, start_pos, rad, thick)
            elif current_tool in ["rtriangle", "etriangle", "rhombus"]:
                pts = get_shape_points(current_tool, start_pos, end_p)
                if pts: pygame.draw.polygon(canvas, current_color, pts, thick)
            drawing = False; last_pos = None

    # Плавное рисование Brush/Eraser (соединяем точки линиями)[cite: 1]
    if drawing and m_pos[1] > 150:
        curr_p = (m_pos[0], m_pos[1]-150)
        if last_pos:
            if current_tool == "brush":
                pygame.draw.line(canvas, current_color, last_pos, curr_p, current_thickness)
                pygame.draw.circle(canvas, current_color, curr_p, current_thickness // 2)
            elif current_tool == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, curr_p, 30)
                pygame.draw.circle(canvas, WHITE, curr_p, 15)
        last_pos = curr_p

    draw_ui()
    if is_typing:
        tf = pygame.font.SysFont(None, current_thickness * 10)
        screen.blit(tf.render(text_input + "|", True, current_color), (text_pos[0], text_pos[1]+150))

    # Live Preview фигур[cite: 1]
    if drawing and m_pos[1] > 150 and current_tool not in ["brush", "eraser"]:
        s_start = (start_pos[0], start_pos[1]+150)
        if current_tool == "line": pygame.draw.line(screen, current_color, s_start, m_pos, current_thickness)
        elif current_tool == "rect":
            r = pygame.Rect(s_start, (m_pos[0]-s_start[0], m_pos[1]-s_start[1]))
            r.normalize(); pygame.draw.rect(screen, current_color, r, thick)
        elif current_tool == "square":
            s = min(abs(m_pos[0]-s_start[0]), abs(m_pos[1]-s_start[1]))
            r = pygame.Rect(s_start, ((1 if m_pos[0]>s_start[0] else -1)*s, (1 if m_pos[1]>s_start[1] else -1)*s))
            r.normalize(); pygame.draw.rect(screen, current_color, r, thick)
        elif current_tool == "circle":
            rad = int(((start_pos[0]-(m_pos[0]))**2 + (start_pos[1]-(m_pos[1]-150))**2)**0.5)
            if rad > 0: pygame.draw.circle(screen, current_color, s_start, rad, thick)
        elif current_tool in ["rtriangle", "etriangle", "rhombus"]:
            pts = get_shape_points(current_tool, start_pos, (m_pos[0], m_pos[1]-150))
            s_pts = [(p[0], p[1] + 150) for p in pts]
            if s_pts: pygame.draw.polygon(screen, current_color, s_pts, thick)

    pygame.display.flip()
pygame.quit()