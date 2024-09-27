import random

import pygame

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCK_WIDTH, BLOCK_HEIGHT = 500, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_ONE = 0
PLAYER_TWO = 0
PLAYER_ONE_LIFES = 1
PLAYER_TWO_LIFES = 1

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Display Word Inside Block")

# Fonts
font = pygame.font.SysFont(None, 48)  # For the word in the block
corner_font = pygame.font.SysFont(None, 36)  # For the text in the corners

# Select a random word from fruits or vegetables list
facts = ["apple", "banana", "orange", "grape", "strawberry"]
nonFacts = ["carrot", "broccoli", "spinach", "potato", "tomato"]
word = random.choice(facts + nonFacts)

# Text for the corners
top_left_text = "Player one: " + str(PLAYER_ONE)
top_right_text = "Player two: " + str(PLAYER_TWO)

# Function to display the block and the word
def draw_block_with_word():
    screen.fill(WHITE)  # Fill the background with white

    # Create a rectangle for the block
    block_rect = pygame.Rect(
        (SCREEN_WIDTH - BLOCK_WIDTH) // 2,
        (SCREEN_HEIGHT - BLOCK_HEIGHT) // 2,
        BLOCK_WIDTH,
        BLOCK_HEIGHT
    )

    # Draw the block (in black for better contrast)
    pygame.draw.rect(screen, BLACK, block_rect)
    pygame.draw.line(screen, BLACK, (400,0), (400, 600))
    # Render the word
    text = font.render(word, True, WHITE)

    # Get the text rectangle and center it inside the block
    text_rect = text.get_rect(center=block_rect.center)

    # Blit (draw) the text onto the screen
    screen.blit(text, text_rect)

    # Render and display the top-left and top-right text
    top_left_surface = corner_font.render(top_left_text, True, BLACK)
    top_right_surface = corner_font.render(top_right_text, True, BLACK)

    # Position the top-left text (small margin from the top-left corner)
    screen.blit(top_left_surface, (10, 10))

    # Position the top-right text (small margin from the top-right corner)
    screen.blit(top_right_surface, (SCREEN_WIDTH - top_right_surface.get_width() - 10, 10))

    # Update the display
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the click is on the left side of the screen
            if mouse_x < SCREEN_WIDTH // 2:
                # Change the variable when the left side is clicked
                PLAYER_ONE += 1
            
            elif mouse_x > SCREEN_WIDTH // 2:
                PLAYER_TWO += 1

    draw_block_with_word()

# Quit pygame
pygame.quit()