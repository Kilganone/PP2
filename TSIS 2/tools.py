import pygame
import math
from collections import deque
from datetime import datetime

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color: return
    queue = deque([(x, y)])
    width, height = surface.get_size()
    while queue:
        curr_x, curr_y = queue.popleft()
        if 0 <= curr_x < width and 0 <= curr_y < height:
            if surface.get_at((curr_x, curr_y)) == target_color:
                surface.set_at((curr_x, curr_y), new_color)
                queue.extend([(curr_x+1, curr_y), (curr_x-1, curr_y), (curr_x, curr_y+1), (curr_x, curr_y-1)])

def get_shape_points(tool, start, end):
    dx, dy = end[0] - start[0], end[1] - start[1]
    if tool == "rtriangle": return [start, (start[0], end[1]), end]
    elif tool == "etriangle":
        side = abs(dx)
        h = (math.sqrt(3) / 2) * side
        dir_y = 1 if dy > 0 else -1
        return [(start[0] + dx // 2, start[1]), (start[0], start[1] + dir_y * h), (start[0] + dx, start[1] + dir_y * h)]
    elif tool == "rhombus":
        return [(start[0] + dx // 2, start[1]), (start[0] + dx, start[1] + dy // 2), 
                (start[0] + dx // 2, start[1] + dy), (start[0], start[1] + dy // 2)]
    return []

def save_canvas(surface):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"paint_save_{timestamp}.png"
    pygame.image.save(surface, filename)
    print(f"Canvas saved as {filename}")