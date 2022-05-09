import pygame

class display:
    """This is where the video output should be coming out
    from.
    """
    def __init__(self, debug = False):
        """Builds a new display from the debug."""
        self._debug = debug

    def close_window(self):
        pygame.display.quit()

    def clear_buffer(self):
        pygame.display.update()
        if self._debug:
            self._draw_grid()

    def open_window(self):
        pygame.display.init()
        pygame.display.set_mode(size=(MAX_HEIGHT,MAX_WIDTH))
        