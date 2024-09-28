import random
import textwrap

import pygame
from PIL import Image

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCK_WIDTH, BLOCK_HEIGHT = 300, 300
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

        # Load GIF and extract frames, scaled to a larger size (e.g., 2x the screen size)
        self.gif_frames, self.gif_offset = self.load_gif_frames('cartoon.gif', scale_factor=1.2)

        # To track the current frame in the animation
        self.current_frame = 0
        self.frame_delay = 15  # Adjust this to slow down the GIF animation
        self.frame_count = 0

        # Word lists
        self.facts = [
            # Easy Tier
            "The Earth is round.",
            "There are seven days in a week.",
            "Plants need sunlight to grow.",
            "The opposite of hot is cold.",
            "Fish live in water.",
            "Birds have wings.",
            "The heart pumps blood through the body.",
            "Leaves on trees are generally green.",
            "Snow is cold.",
            "Fire is hot.",
            "A year has twelve months.",
            "An orange is a type of fruit.",
            "Dogs are mammals.",
            "Water freezes at 0 degrees Celsius.",
            "The sky appears blue during a sunny day.",
            "Honey is made by bees.",
            "An apple is a fruit.",
            "Cats have whiskers.",
            "Humans need oxygen to breathe.",
            "A bicycle has two wheels.",
            "Water boils at 100 degrees Celsius at sea level.",
            "The Earth revolves around the Sun.",
            "Humans have 46 chromosomes.",
            "The chemical formula for water is H2O.",
            "Sharks are a type of fish.",
            "The capital of France is Paris.",
            "Octopuses have three hearts.",
            "Photosynthesis is the process plants use to make food from sunlight.",
            "Diamond is the hardest natural substance on Earth.",
            "A group of crows is called a murder.",
            "The largest ocean on Earth is the Pacific Ocean.",
            "Bats are mammals.",
            "The human body has 206 bones.",
            "Venus is the hottest planet in the solar system.",
            "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
            "The Great Wall of China is visible from space.",
            "An octagon has eight sides.",
            "Albert Einstein developed the theory of relativity.",
            "The Pacific Ring of Fire is famous for its volcanic and seismic activity.",
            "Antarctica is the driest continent on Earth.",
            # Medium Tier
            "Jupiter has the most moons of any planet in the solar system.",
            "The inventor of the light bulb, Thomas Edison, held over 1,000 patents.",
            "Coffee is derived from berries.",
            "An adult human skeleton typically accounts for about 14% of the body's total weight.",
            "Woolly mammoths still walked the earth when the Great Pyramid was being constructed.",
            "All squares are rectangles, but not all rectangles are squares.",
            "Helium is the second lightest and second most abundant element in the observable universe.",
            "The deadliest war in history, in terms of the number of people killed, was World War II.",
            "Honey never spoils.",
            "The largest desert in the world is Antarctica.",
            # More medium facts...
            # Difficult Tier
            "The sum of all natural numbers (1 + 2 + 3 + ...) is -1/12 in certain mathematical contexts.",
            "Cleopatra lived closer in time to the moon landing than to the construction of the Great Pyramid of Giza.",
            "Venus rotates on its axis in a direction opposite to that of most planets in the solar system.",
            "The strongest muscle in the human body based on its weight is the masseter (jaw muscle).",
            "The Eiffel Tower can be 15 cm taller during the summer when the metal expands due to heat.",
            "Bananas are berries, but strawberries are not.",
            # More difficult facts...
        ]
        self.non_facts = [
             # Easy Tier
            "Cars can fly.",
            "Fish can live out of water.",
            "Chocolate milk comes from black cows.",
            "All birds can talk.",
            "Humans can breathe underwater without help.",
            "Cats are a type of bird.",
            "Deserts are always cold.",
            "A minute has 100 seconds.",
            "Trees can walk.",
            "The sun rises in the west.",
            "All dogs can swim.",
            "Apples are vegetables.",
            "Ice is heavier than water.",
            "Penguins live in the Sahara Desert.",
            "The moon is made of cheese.",
            "All plants are blue.",
            "Rabbits can fly.",
            "A year has 10 months.",
            "Humans can see ultraviolet light naturally.",
            "The Earth is flat.",
            "Cats have nine lives.",
            "Humans can breathe in space without assistance.",
            "The sun revolves around the Earth.",
            "Chocolate milk comes from brown cows.",
            "Penguins can fly.",
            "The capital of Spain is Barcelona.",
            "All insects have six legs.",
            "Goldfish have a three-second memory.",
            "Dogs can only see in black and white.",
            "The largest country in the world by area is the United States.",
            # Medium Tier
            "The human brain is fully mature by the time a person reaches 18 years of age.",
            "Lightning never strikes the same place twice.",
            "Humans can see millions of colors.",
            "The Great Pyramid of Giza was built by slaves.",
            "Ostriches bury their heads in the sand when they are scared.",
            "More than 50% of the human body's cells are human cells.",
            "The Titanic was deemed 'unsinkable' before setting sail.",
            "You can see the Great Wall of China from the moon.",
            "A penny dropped from the Empire State Building can kill someone.",
            "The full moon affects human behavior.",
            # More medium facts...
            # Difficult Tier
            "Vitamin C prevents common colds.",
            "Shaving hair makes it grow back thicker and darker.",
            "Humans use only 10% of their brains.",
            "Drinking alcohol kills brain cells.",
            "Sushi means 'raw fish' in Japanese.",
            "The Forbidden City is in Shanghai.",
            "The Pythagorean theorem applies to all types of triangles.",
            "You can catch a cold from cold weather.",
            "Deoxygenated blood is blue.",
            "Eating at night makes you gain weight faster than eating the same food during the day.",
            # More difficult facts...
        ]

        # Select an initial word
        self.select_new_word()

    def load_gif_frames(self, gif_path, scale_factor=2):
        """Load GIF frames using Pillow, scale them to a larger size, and center."""
        gif = Image.open(gif_path)
        frames = []
        new_width = int(SCREEN_WIDTH * scale_factor)
        new_height = int(SCREEN_HEIGHT * scale_factor)

        # Calculate offsets to center the GIF
        offset_x = (SCREEN_WIDTH - new_width) // 2
        offset_y = (SCREEN_HEIGHT - new_height) // 2

        try:
            while True:
                frame = gif.copy()
                frame = frame.convert("RGBA")  # Convert to a Pygame-compatible format

                # Resize frame to a larger dimension using the scale factor
                frame = frame.resize((new_width, new_height), Image.ANTIALIAS)

                # Convert to Pygame surface
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()

                pygame_image = pygame.image.fromstring(data, size, mode)
                frames.append(pygame_image)

                # Move to the next frame
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass  # End of GIF frames
        
        # Return the frames and the offset needed to center the larger image
        return frames, (offset_x, offset_y)

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

    def update_frame(self):
        """Update the GIF frame."""
        if self.frame_count == self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
            self.frame_count = 0
        else:
            self.frame_count += 1

    def draw(self, player_one_score, player_two_score, player_one_lifes, player_two_lifes):
        """Draw the block with the word, list name, and player scores."""
        # Update the background frame
        self.update_frame()

        # Draw the current frame of the background GIF, scaled and centered
        offset_x, offset_y = self.gif_offset
        self.screen.blit(self.gif_frames[self.current_frame], (offset_x, offset_y))

        # Create the block rectangle
        block_rect = pygame.Rect(
            (SCREEN_WIDTH - BLOCK_WIDTH) // 2,
            (SCREEN_HEIGHT - BLOCK_HEIGHT) // 2,
            BLOCK_WIDTH,
            BLOCK_HEIGHT
        )

        # Draw the block (black rectangle)
        pygame.draw.rect(self.screen, BLACK, block_rect)
        pygame.draw.line(self.screen, BLACK, (400, 0), (400, 600), width=2)

        # Render the word inside the block
        word_text = f"{self.word}"  # Show word and the list name

        # Split the text into words and wrap text
        words = word_text.split(' ')
        lines = []
        current_line = []
        current_width = 0

        # Calculate width for each word and wrap if necessary
        for word in words:
            word_surface = self.font.render(word + ' ', True, WHITE)  # Add a space after each word
            word_width, word_height = word_surface.get_size()

            if current_width + word_width <= BLOCK_WIDTH:
                current_line.append(word)
                current_width += word_width
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_width = word_width

        # Append the last line
        if current_line:
            lines.append(' '.join(current_line))

        # Render each line of the wrapped text and ensure it fits within the block
        line_height = self.font.size('Tg')[1]  # Approximate height of one line
        total_text_height = len(lines) * line_height

        # Start drawing text from the top of the block, centered vertically
        start_y = block_rect.centery - total_text_height // 2

        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, WHITE)
            text_rect = text_surface.get_rect(center=(block_rect.centerx, start_y + i * line_height))
            self.screen.blit(text_surface, text_rect)

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
