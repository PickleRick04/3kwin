import random

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCK_WIDTH, BLOCK_HEIGHT = 500, 300
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Look:
    """Class to handle the rendering and visual representation of the game."""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Quiz game")

        # Fonts for rendering
        self.font = pygame.font.SysFont(None, 48)
        self.corner_font = pygame.font.SysFont(None, 36)

        # Initialize word selection (can be updated dynamically)
        self.word = ""
        self.word_list_name = ""

        # Load background image
        self.background_image = pygame.image.load('Background.jpg').convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Word lists
        self.facts = ["apple", "banana", "orange", "grape", "strawberry"]
        self.non_facts = ["carrot", "broccoli", "spinach", "potato", "tomato"]

        # Select an initial word
        self.select_new_word()

    def select_new_word(self):
        """Select a new random word and determine whether it's from the facts or nonFacts list."""
        combined_list = self.facts + self.non_facts
        self.word = random.choice(combined_list)

        # Determine whether the word came from the facts or nonFacts list
        if self.word in self.facts:
            self.facts.remove(self.word)
            self.word_list_name = "facts"
        else:
            self.non_facts.remove(self.word)
            self.word_list_name = "non_facts"

    def draw(self, player_one_score, player_two_score, player_one_lifes, player_two_lifes):
        """Draw the block with the word, list name, and player scores."""
        # Draw the background image
        self.screen.blit(self.background_image, (0, 0))

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
        word_text = f"{self.word} ({self.word_list_name})"  # Show word and the list name
        text = self.font.render(word_text, True, WHITE)
        text_rect = text.get_rect(center=block_rect.center)
        self.screen.blit(text, text_rect)

        # Render player scores in the corners
        top_left_text = f"Points: {player_one_score}"
        top_right_text = f"Points: {player_two_score}"
        bottom_left_text = f"Lifes: {player_one_lifes}"
        bottom_right_text = f"Lifes: {player_two_lifes}"

        top_left_surface = self.corner_font.render(top_left_text, True, WHITE)
        top_right_surface = self.corner_font.render(top_right_text, True, WHITE)
        bottom_left_surface = self.corner_font.render(bottom_left_text, True, WHITE)
        bottom_right_surface = self.corner_font.render(bottom_right_text, True, WHITE)

        self.screen.blit(top_left_surface, (10, 10))
        self.screen.blit(top_right_surface, (SCREEN_WIDTH - top_right_surface.get_width() - 10, 10))
        self.screen.blit(bottom_left_surface, (10, SCREEN_HEIGHT - bottom_left_surface.get_height() - 10))
        self.screen.blit(bottom_right_surface, (SCREEN_WIDTH - top_right_surface.get_width() - 10, SCREEN_HEIGHT - bottom_left_surface.get_height() - 10))

        # Update the display
        pygame.display.flip()