import pygame
import random
from start_screen import start_screen

# Initialize Pygame
pygame.init()

# Set the window size
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake.io')

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

# Define the function to draw the snake and obstacles
def draw_snake(snake_block_size, snake_list, obstacles):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block_size, snake_block_size])
    for obs in obstacles:
        pygame.draw.rect(window, black, [obs[0], obs[1], obs[2], block_size])

# Define the function to generate new obstacles
def generate_obstacles(score):
    obstacles = []
    if score % 1 == 0:
        num_obstacles = random.randint(1, 5)
        for i in range(num_obstacles):
            obs_width = random.randint(2, 10) * block_size
            obs_height = block_size
            obs_x = random.randint(0, (window_width - obs_width) // block_size) * block_size
            obs_y = random.randint(0, (window_height - obs_height) // block_size) * block_size
            obstacles.append((obs_x, obs_y, obs_width))
    return obstacles

# Define the game loop
def game_loop():
    # Initialize game variables
    game_over = False
    game_close = False
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
    score = 0
    obstacles = []

    while not game_over:

        # Game over loop
        while game_close:
            window.fill(white)
            message_to_screen("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            #User input check after losing
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        # events check
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
        for obstacle in obstacles:
            if obstacle[0] == x1 and obstacle[1] == y1:
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

        # Draw the snake and obstacles
        draw_snake(block_size, snake_List, obstacles)

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
            obstacles = generate_obstacles(score)

        

        # Set the game clock
        clock = pygame.time.Clock()

        # Set the game speed
        snake_speed = 15

        # Limit the game speed
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()


# Start the start screen
start_screen()
# Start the game loop
game_loop()