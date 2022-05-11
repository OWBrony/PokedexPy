from Display import display 
from Constants import *
from sys import exit

class director:
    
    def __init__(self):
        """Creates new instance of director"""
        self._video_service = display()
        self.run = True

    def run_game(self):
        run = True
        while run:
            self._video_service.open_window()
            run = self._video_service.is_running()
        self._video_service.close_window()
