from Display import display 
from Constants import *

class director:
    
    def __init__(self):
        """Creates new instance of director"""
        self._video_service = display()

    def run_game(self):
        while self._video_service.is_running:
            self._video_service.open_window(self)
        self._video_service.close_window
