# look.py
import random

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCK_WIDTH, BLOCK_HEIGHT = 500, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Look:
    """Class to handle the rendering and visual representation of the game."""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Display Word Inside Block")

        # Fonts for rendering
        self.font = pygame.font.SysFont(None, 48)
        self.corner_font = pygame.font.SysFont(None, 36)

        # Word selection
        fruits = ["apple", "banana", "orange", "grape", "strawberry"]
        vegetables = ["carrot", "broccoli", "spinach", "potato", "tomato"]
        self.word = random.choice(fruits + vegetables)

    def draw(self, player_one_score, player_two_score):
        """Draw the block with the word and player scores."""
        self.screen.fill(WHITE)

        # Create the block rectangle
        block_rect = pygame.Rect(
            (SCREEN_WIDTH - BLOCK_WIDTH) // 2,
            (SCREEN_HEIGHT - BLOCK_HEIGHT) // 2,
            BLOCK_WIDTH,
            BLOCK_HEIGHT
        )

        # Draw the block (black rectangle)
        pygame.draw.rect(self.screen, BLACK, block_rect)
        pygame.draw.line(self.screen, BLACK, (400, 0), (400, 600))

        # Render the word inside the block
        text = self.font.render(self.word, True, WHITE)
        text_rect = text.get_rect(center=block_rect.center)
        self.screen.blit(text, text_rect)

        # Render player scores in the corners
        top_left_text = f"Player one: {player_one_score}"
        top_right_text = f"Player two: {player_two_score}"

        top_left_surface = self.corner_font.render(top_left_text, True, BLACK)
        top_right_surface = self.corner_font.render(top_right_text, True, BLACK)

        self.screen.blit(top_left_surface, (10, 10))
        self.screen.blit(top_right_surface, (SCREEN_WIDTH - top_right_surface.get_width() - 10, 10))

        # Update the display
        pygame.display.flip()
