import pygame
from pygame.locals import K_a, K_l

SCREEN_WIDTH = 800

class Reaction:
    """Class to handle player interactions and score updates."""
    def __init__(self, look):
        self.button = False
        self.player_one_score = 0
        self.player_two_score = 0
        self.player_one_lifes = 3
        self.player_two_lifes = 3
        self.look = look  # Pass the Look instance to be able to change the word

    def handle_event(self, event):
        self.button = False
        """Handles mouse click events to update player scores."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.button = True
            mouse_x, _ = pygame.mouse.get_pos()

            # Update the score based on click position
            if mouse_x < SCREEN_WIDTH // 2:
                if self.look.word_list_name == "facts":  # Check against the correct string
                    self.player_one_score += 1
                else:
                    self.player_one_lifes -= 1
            else:
                if self.look.word_list_name == "facts":  # Check against the correct string
                    self.player_two_score += 1
                    
                else:
                    self.player_two_lifes -= 1

            # Select a new word after each click and identify the list
            self.look.select_new_word()
            
        #elif event.type == pygame.KEYDOWN:
        #    if event.key == K_a:
        #        self.button = True
        #    # Player one scores if correct word list
        #        if self.look.word_list_name == "facts":
        #            self.player_one_score += 1
        #        else:
        #            self.player_one_lifes -= 1
        #    elif event.key == K_l:
        #        self.button = True
            # Player two scores if correct word list
        #        if self.look.word_list_name == "facts":
        #            self.player_two_score += 1
        #        else:
        #            self.player_two_lifes -= 1

        # Select a new word after key press
        #    self.look.select_new_word()
    def get_scores(self):
        """Returns the current player scores."""
        return self.player_one_score, self.player_two_score
    def get_lifes(self):
        """Returns the current player scores."""
        return self.player_one_lifes, self.player_two_lifes
    