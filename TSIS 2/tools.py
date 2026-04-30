import pygame
import math
from collections import deque
from datetime import datetime

def flood_fill(surface, x, y, new_color):
    """
    Standard Breadth-First Search (BFS) algorithm to fill a closed area with color.
   
    """
    # Get the color of the pixel where the user clicked
    target_color = surface.get_at((x, y))
    
    # If the area is already the target color, exit to prevent infinite loop
    if target_color == new_color: return
    
    # Initialize queue for BFS and get surface boundaries
    queue = deque([(x, y)])
    width, height = surface.get_size()
    
    while queue:
        curr_x, curr_y = queue.popleft()
        
        # Check if coordinates are within the canvas limits
        if 0 <= curr_x < width and 0 <= curr_y < height:
            # If current pixel matches the color we want to replace
            if surface.get_at((curr_x, curr_y)) == target_color:
                # Change pixel color
                surface.set_at((curr_x, curr_y), new_color)
                
                # Add all 4 neighboring pixels (Right, Left, Down, Up) to the queue
                queue.extend([
                    (curr_x + 1, curr_y), 
                    (curr_x - 1, curr_y), 
                    (curr_x, curr_y + 1), 
                    (curr_x, curr_y - 1)
                ])

def get_shape_points(tool, start, end):
    """
    Calculates vertex coordinates for complex polygons based on mouse drag.
   
    """
    dx, dy = end[0] - start[0], end[1] - start[1]
    
    # Right-angled triangle: Start, Corner (perpendicular), and End point
    if tool == "rtriangle": 
        return [start, (start[0], end[1]), end]
    
    # Equilateral triangle logic
    elif tool == "etriangle":
        side = abs(dx)
        # Height of an equilateral triangle: h = (sqrt(3)/2) * side
        h = (math.sqrt(3) / 2) * side
        dir_y = 1 if dy > 0 else -1
        # Returns: Top-middle, Bottom-left, Bottom-right vertices
        return [
            (start[0] + dx // 2, start[1]), 
            (start[0], start[1] + dir_y * h), 
            (start[0] + dx, start[1] + dir_y * h)
        ]
    
    # Rhombus (Diamond): Points at the center-top, right-middle, center-bottom, and left-middle
    elif tool == "rhombus":
        return [
            (start[0] + dx // 2, start[1]),           # Top center
            (start[0] + dx, start[1] + dy // 2),      # Right middle
            (start[0] + dx // 2, start[1] + dy),      # Bottom center
            (start[0], start[1] + dy // 2)            # Left middle
        ]
    return []

def save_canvas(surface):
    """
    Generates a unique filename using the current date and time and saves the image.
   
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"paint_save_{timestamp}.png"
    
    # Pygame's built-in method to export the Surface as an image file
    pygame.image.save(surface, filename)
    print(f"Canvas saved as {filename}")