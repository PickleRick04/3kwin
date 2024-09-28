import pygame

from look import Look
from reaction import Reaction


class Game:
    """Main game logic controller."""
    def __init__(self):
        self.look = Look()
        self.reaction = Reaction(self.look) 
        self.running = True
        self.font = pygame.font.SysFont(None, 72) 
        self.last_word_update = pygame.time.get_ticks() 

    def run(self):
        """Main game loop that keeps the game running."""
        while self.running:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.reaction.handle_event(event)
                
            if self.reaction.button:
                self.last_word_update = current_time

            # update word every 5 sek
            if current_time - self.last_word_update > 5000 and not self.reaction.word_updates_paused:
                self.look.select_new_word()
                self.last_word_update = current_time  

            player_one_score, player_two_score = self.reaction.get_scores()
            player_one_lifes, player_two_lifes = self.reaction.get_lifes()

            if player_one_lifes == 0 or player_two_lifes == 0:
                self.running = False 

            self.look.draw(player_one_score, player_two_score, player_one_lifes, player_two_lifes)

        self.show_end_screen(player_one_score, player_two_score)

        pygame.quit()

    def show_end_screen(self, player_one_score, player_two_score):
        """Displays the end screen with the winner and the final scores."""
        winner = "Player 1" if player_one_score > player_two_score else "Player 2"
        if player_one_score == player_two_score:
            winner = "It's a Tie!"

        self.look.screen.fill((255, 255, 255))

        if winner != "It's a Tie!":
            end_message = f"{winner} Wins!"
        else:
            end_message = "It's a Tie!"
            
        score_message = f"{player_one_score} : {player_two_score}"
        end_text = self.font.render(end_message, True, (0, 0, 0))
        score_text = self.font.render(score_message, True, (0, 0, 0))

        end_rect = end_text.get_rect(center=(400, 200))
        score_rect = score_text.get_rect(center=(400, 300))
        self.look.screen.blit(end_text, end_rect)
        self.look.screen.blit(score_text, score_rect)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False