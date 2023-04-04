import pygame

pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up fonts
FONT_SIZE = 50
font = pygame.font.SysFont(None, FONT_SIZE)

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_text(text, font, color, x, y):
    """Helper function to draw text onto the screen."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

def start_screen():
    """Displays the start screen of the game."""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        # Clear the screen
        window.fill(WHITE)

        # Draw title text
        draw_text("Snake Game", font, BLACK, WINDOW_WIDTH/2, WINDOW_HEIGHT/4)

        # Draw instructions text
        draw_text("Press SPACE to start", font, BLACK, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

        pygame.display.update()

start_screen()