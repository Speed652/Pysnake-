import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define the size of the blocks
block_size = 10

# Define the font
font = pygame.font.SysFont(None, 25)

# Define the function to display the message on the screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, [window_width/6, window_height/2])

# Define the function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block_size, snake_block_size])

# Define the game loop
def game_loop():
    # Set the game variables
    game_over = False
    game_close = False

    # Set the starting position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Set the change in position of the snake
    x1_change = 0       
    y1_change = 0

    # Set the snake list and length
    snake_List = []
    Length_of_snake = 1

    # Set the position of the food
    foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

    # Game loop
    while not game_over:

        # Game over loop
        while game_close == True:
            window.fill(white)
            message_to_screen("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Check for user input after losing
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Check for events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check if the snake hits the border of the window
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Fill the window with white
        window.fill(white)
        
        # Draw the food
        pygame.draw.rect(window, red, [foodx, foody, block_size, block_size])

        # Update the snake's length when it eats the food
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake
        draw_snake(block_size, snake_List)

        # Update the score
        score = Length_of_snake - 1
        score_font = font.render("Score: " + str(score), True, black)
        window.blit(score_font, [0, 0])

        # Update the window
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        # Set the game clock
        clock = pygame.time.Clock()

        # Set the game speed
        snake_speed = 15

        # Limit the game speed
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()

# Start the game loop
game_loop()