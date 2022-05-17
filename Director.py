import pygame
from services.Display import display 
from Constants import *
from items.artifact import Artifact
from items.image import Image

class director:
    
    def __init__(self):
        """Creates new instance of director"""
        self._video_service = display()
        self.run = True

    def run_game(self):
        run = True
        current_pokemon = Image()
        current_pokemon.get_image(IMAGE_DEFAULT)
        self._video_service.open_window()
        while run:
            # This checks for the user closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # This is to display the image that was chosen
            current_pokemon.show_image()
            # this is to hopefully refresh the screen
            self._video_service.clear_buffer()
            # run = self._video_service.is_running()
        self._video_service.close_window()
