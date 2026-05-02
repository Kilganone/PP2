import pygame

# ---------------- COLORS ---------------- #

# Basic UI colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (90, 90, 90)
BLUE = (55, 110, 185)
RED = (190, 70, 70)

# ---------------- BUTTON CLASS ---------------- #

class Button:
    """Reusable UI button with hover and click detection"""

    def __init__(self, rect, text, action, color=GRAY):
        # Button position and size
        self.rect = pygame.Rect(rect)

        # Text displayed on the button
        self.text = text

        # Action identifier (used in main logic)
        self.action = action

        # Default button color
        self.color = color

    def draw(self, surface, font):
        """Draw button with hover effect"""
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is over button
        is_hovered = self.rect.collidepoint(mouse_pos)

        # Change color on hover
        fill_color = DARK_GRAY if is_hovered else self.color

        # Draw button background
        pygame.draw.rect(surface, fill_color, self.rect, border_radius=8)

        # Draw border
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=8)

        # Render text (invert color on hover for better contrast)
        text_image = font.render(self.text, True, WHITE if is_hovered else BLACK)

        # Center text inside button
        text_rect = text_image.get_rect(center=self.rect.center)

        surface.blit(text_image, text_rect)

    def is_clicked(self, event):
        """Check if button was clicked (left mouse button)"""
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

# ---------------- TEXT DRAWING ---------------- #

def draw_center_text(surface, text, font, color, center):
    """Draw text centered at given position"""
    image = font.render(text, True, color)
    rect = image.get_rect(center=center)
    surface.blit(image, rect)

def draw_left_text(surface, text, font, color, pos):
    """Draw text aligned to top-left corner"""
    image = font.render(text, True, color)
    surface.blit(image, pos)

# ---------------- PANEL ---------------- #

def draw_panel(surface, rect, fill_color=(240, 240, 240)):
    """Draw rounded panel with border (used for UI blocks)"""
    panel_rect = pygame.Rect(rect)

    # Fill panel
    pygame.draw.rect(surface, fill_color, panel_rect, border_radius=10)

    # Draw border
    pygame.draw.rect(surface, BLACK, panel_rect, 2, border_radius=10)

# ---------------- MENU ---------------- #

def make_menu_buttons():
    """Create main menu buttons"""
    return [
        Button((110, 180, 180, 44), "Play", "play", BLUE),
        Button((110, 240, 180, 44), "Leaderboard", "leaderboard", BLUE),
        Button((110, 300, 180, 44), "Settings", "settings", BLUE),
        Button((110, 360, 180, 44), "Quit", "quit", RED),
    ]