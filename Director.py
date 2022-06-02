import pygame
from services.Display import display 
from Constants import *
from items.artifact import Artifact
from items.image import Image
from items.Text_Box import text_box
from scroll_bar import scroller
from resources.kanto_dex import *
from

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
        text_bar = text_box(self._video_service)
        # kanto_scrollbar = scroller(kanto_list, "kanto")
        while run:
            # This checks for the user closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_bar.collidepoint(event.pos):
                        text_bar.active = True
                    else:
                        text_bar.active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text_bar.user_text = text_bar.user_text[:-1]
            # This is to display the image that was chosen
            current_pokemon.show_image()
            # kanto_scrollbar
            # this is to hopefully refresh the screen
            self._video_service.clear_buffer()
            # run = self._video_service.is_running()
        self._video_service.close_window()
