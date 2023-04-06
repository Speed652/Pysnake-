import pygame
from options import options_screen

pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake.io")

# Set up fonts
FONT_FOLDER = "fonts"
TITLE_FONT_SIZE = 80
BUTTON_FONT_SIZE = 50
title_font = pygame.font.Font(f"{FONT_FOLDER}/Roboto-Bold.ttf", TITLE_FONT_SIZE)
button_font = pygame.font.Font(f"{FONT_FOLDER}/Roboto-Regular.ttf", BUTTON_FONT_SIZE)


image_path = "assets/peakpx.jpg"
image = pygame.image.load(image_path)

# Set up colors
BACKGROUND_COLOR = (68, 74, 88)
TITLE_COLOR = (240, 240, 240)
BUTTON_COLOR = (250, 250, 250)
BUTTON_BORDER_COLOR = (180, 180, 180)
BUTTON_BORDER_WIDTH = 5


def draw_text(text, font, color, x, y):
    """Helper function to draw text onto the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    window.blit(text_surface, text_rect)


def draw_button(text, font, bg_color, border_color, x, y, width, height, selected):
    """Helper function to draw a button onto the screen."""
    button_rect = pygame.Rect(x, y, width, height)
    button_color = bg_color if not selected else border_color
    pygame.draw.rect(window, button_color, button_rect)
    pygame.draw.rect(window, border_color, button_rect, BUTTON_BORDER_WIDTH)
    draw_text(text, font, BUTTON_BORDER_COLOR, x + width / 2, y + height / 2)


def start_screen():
    """Displays the start screen of the game."""
    buttons = ["START", "QUIT"]
    selected_button = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_button = (selected_button + 1) % len(buttons)
                elif event.key == pygame.K_UP:
                    selected_button = (selected_button - 1) % len(buttons)
                elif event.key == pygame.K_SPACE:
                    if selected_button == 0:
                        running = False
                    elif selected_button == 1:
                        options_screen()
                    elif selected_button == 2:
                        pygame.quit()
                        quit()

        # Clear the screen
        window.blit(image, (0, 0))
        
        # Draw title text
        draw_text("Snake.io", title_font, TITLE_COLOR, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 6)

        # Draw buttons
        button_width = 200
        button_height = 75
        button_spacing = 50
        total_button_height = (button_height + button_spacing) * len(buttons) - button_spacing
        buttons_y = (WINDOW_HEIGHT - total_button_height) / 2
        
        for i, button_text in enumerate(buttons):
            button_x = WINDOW_WIDTH / 2 - button_width / 2
            button_y = buttons_y + i * (button_height + button_spacing)
            selected = (i == selected_button)
            draw_button(button_text, button_font, BUTTON_COLOR, BUTTON_BORDER_COLOR,
                        button_x, button_y, button_width, button_height, selected)

        pygame.display.update()


start_screen()