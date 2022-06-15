import pygame
from Constants import *

class display:
    """This is where the video output should be coming out
    from.
    """
    def __init__(self, debug = False):
        """Builds a new display from the debug."""
        self._debug = debug
        self.running = True
        self.display = pygame.display.init()

    def close_window(self):
        pygame.display.quit()

    def clear_buffer(self):
        pygame.display.update()
        if self._debug:
            self._draw_grid()

    def open_window(self):
        pygame.display.set_mode(SCREEN_SIZE)

    def clear_window(self):
        pygame.Surface.fill(self, (0,0,0))
        
    def draw_image(self, image, position):
        """Draws the given image on the buffer at the given position. The image won't appear
        on the screen until flush_buffer() is called.

        Args:
            image: An instance of batter.casting.image.
            position: An instance of a point.

        Raises:
            KeyError: If the image file hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_text(self, text, position):
        """Draws the given text on the buffer at the given position. The text won't appear
        on the screen until flush_buffer() is called.

        Args:
            text: An instance of batter.casting.text.
            position: An instance of batter.casting.point.

        Raises:
            KeyError: If the font file for the text hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")

    

    def _draw_grid():
        pass