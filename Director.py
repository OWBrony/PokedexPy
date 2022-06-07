import pygame
from services.Display import display 
from Constants import *
from items.artifact import Artifact
from items.image import Image
from items.Text_Box import text_box
from scroll_bar import scroller
from resources.kanto_dex import *


class director:
    
    def __init__(self):
        """Creates new instance of director"""
        self._video_service = display()
        self.run = True

    def run_game(self):
        clock = pygame.time.Clock()
        run = True
        # this is to set the current pokemon's image.
        current_pokemon = Image()
        # This is to set the default for the window opening.
        current_pokemon.get_image(IMAGE_DEFAULT)
        # This is to open the window
        self._video_service.open_window()
        # This is meant to initialize the search bar.
        text_bar = text_box(self._video_service)
        while run:
            # This checks for the user closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # This is to check if the user clicked on the search bar
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_bar.collide_point(pygame.mouse.get_pos):
                        text_bar.active = True
                        text_bar.select_color()
                    else:
                        text_bar.active = False
                        text_bar.select_color()
                # This is to check if a key was pressed.
                if event.type == pygame.KEYDOWN:
                    # if backspace remove a letter
                    if event.key == pygame.K_BACKSPACE:
                        text_bar.user_text = text_bar.user_text[:-1]
                    else:
                        text_bar.user_text += event.unicode
            text_bar.draw_rect(self._video_service)
            # This is to display the image that was chosen
            current_pokemon.show_image()
            # kanto_scrollbar
            # this is to hopefully refresh the screen
            self._video_service.clear_buffer()
            # run = self._video_service.is_running()
            clock.tick(60)
        self._video_service.close_window()
