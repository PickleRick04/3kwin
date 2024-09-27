# game.py
import pygame

from look import Look
from reaction import Reaction


class Game:
    """Main game logic controller."""
    def __init__(self):
        self.look = Look()
        self.reaction = Reaction(self.look)  # Pass the Look instance to Reaction
        self.running = True

    def run(self):
        """Main game loop that keeps the game running."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Let Reaction handle player input
                self.reaction.handle_event(event)

            # Get the updated scores
            player_one_score, player_two_score = self.reaction.get_scores()

            # Let Look handle the rendering of the game state
            self.look.draw(player_one_score, player_two_score)

        pygame.quit()
#COMMENT