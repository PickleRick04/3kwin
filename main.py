# main.py
import pygame

from game import Game

if __name__ == "__main__":
    # Initialize pygame before running the game
    pygame.init()

    # Start the game
    game = Game()

    game.run()

    # Quit pygame after the game loop ends
    pygame.quit()