import pygame
from pygame.locals import K_a, K_l, K_v

SCREEN_WIDTH = 800

class Reaction:
    """Class to handle player interactions and score updates."""
    def __init__(self, look):
        self.button = False
        self.player_one_score = 0
        self.player_two_score = 0
        self.player_one_lifes = 3
        self.player_two_lifes = 3
        self.look = look 
        self.word_updates_paused = False

    def handle_event(self, event):
        """Handles mouse click and key press events to update player scores."""
        self.button = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.button = True
            mouse_x, _ = pygame.mouse.get_pos()
            if mouse_x < SCREEN_WIDTH // 2:
                self.update_player_score(is_left=True)
            else:
                self.update_player_score(is_left=False)
            
            if not self.word_updates_paused:
                self.look.select_new_word()
        elif event.type == pygame.KEYDOWN:
            self.handle_key_press(event)


    def handle_key_press(self, event):
        """Handles key press event logic."""
        if event.key == K_a:
            self.button = True
            self.update_player_score(is_left=True)
            self.look.select_new_word()
        elif event.key == K_l:
            self.button = True
            self.update_player_score(is_left=False)
            self.look.select_new_word()
        elif event.key == K_v:
            self.word_updates_paused = not self.word_updates_paused
        

    def update_player_score(self, is_left):
        """Updates score or lives based on the word list and player side."""
        if is_left:
            if self.look.word_list_name == "facts":
                self.player_one_score += 1
            else:
                self.player_one_lifes -= 1
        else:
            if self.look.word_list_name == "facts":
                self.player_two_score += 1
            else:
                self.player_two_lifes -= 1

    def get_scores(self):
        """Returns the current player scores."""
        return self.player_one_score, self.player_two_score

    def get_lifes(self):
        """Returns the current player lives."""
        return self.player_one_lifes, self.player_two_lifes
    
    