import pygame

from look import Look
from reaction import Reaction


class Game:
    """Main game logic controller."""
    def __init__(self):
        self.look = Look()
        self.reaction = Reaction(self.look)  # Pass the Look instance to Reaction
        self.running = True
        self.font = pygame.font.SysFont(None, 72)  # Font for the end screen
        self.last_word_update = pygame.time.get_ticks()  # Track the last word update time

    def run(self):
        """Main game loop that keeps the game running."""
        while self.running:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Let Reaction handle player input
                self.reaction.handle_event(event)

            if self.reaction.button:
                self.last_word_update = current_time
            # Check if 5 seconds have passed to update the word
            if current_time - self.last_word_update > 5000:
                self.look.select_new_word()
                self.last_word_update = current_time  # Reset the word update timer

            # Get the updated scores and lives
            player_one_score, player_two_score = self.reaction.get_scores()
            player_one_lifes, player_two_lifes = self.reaction.get_lifes()

            # Check if the game should end
            if player_one_lifes == 0 or player_two_lifes == 0:
                self.running = False  # Stop the game loop

            # Let Look handle the rendering of the game state
            self.look.draw(player_one_score, player_two_score, player_one_lifes, player_two_lifes)

        # Show the end screen after the game loop ends
        self.show_end_screen(player_one_score, player_two_score)

        pygame.quit()

    def show_end_screen(self, player_one_score, player_two_score):
        """Displays the end screen with the winner and the final scores."""
        winner = "Player 1" if player_one_score > player_two_score else "Player 2"
        if player_one_score == player_two_score:
            winner = "It's a Tie!"

        # Fill the screen with white
        self.look.screen.fill((255, 255, 255))

        # Display the winner and the final scores
        if winner != "It's a Tie!":
            end_message = f"{winner} Wins!"
        else:
            end_message = "It's a Tie!"
            
        score_message = f"{player_one_score} : {player_two_score}"
        end_text = self.font.render(end_message, True, (0, 0, 0))
        score_text = self.font.render(score_message, True, (0, 0, 0))

        # Center the text on the screen
        end_rect = end_text.get_rect(center=(400, 200))
        score_rect = score_text.get_rect(center=(400, 300))

        # Draw the text on the screen
        self.look.screen.blit(end_text, end_rect)
        self.look.screen.blit(score_text, score_rect)

        # Update the display
        pygame.display.flip()

        # Keep the end screen visible until the user closes the game
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
