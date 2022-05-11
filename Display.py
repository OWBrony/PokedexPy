import pygame
from Constants import *
from sys import exit

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
        pygame.display.set_mode(size=(800,600))

    def is_running(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

    def _draw_grid():
        pass
        