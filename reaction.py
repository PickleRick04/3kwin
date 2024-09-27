# reaction.py
import pygame

SCREEN_WIDTH = 800

class Reaction:
    """Class to handle player interactions and score updates."""
    def __init__(self):
        self.player_one_score = 0
        self.player_two_score = 0

    def handle_event(self, event):
        """Handles mouse click events to update player scores."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, _ = pygame.mouse.get_pos()

            # Update the score based on click position
            if mouse_x < SCREEN_WIDTH // 2:
                self.player_one_score += 1
            else:
                self.player_two_score += 1

    def get_scores(self):
        """Returns the current player scores."""
        return self.player_one_score, self.player_two_score
