import pygame
from items.artifact import Artifact
from Constants import *

import requests
import json
import io
class Image(Artifact):
    def __init__(self, x=0, y=0):
        self.image = ""
        self.comparison = None
        self.image_from_URL = None
        self.position = ()
        self._x = x
        self._y = y
        self.display_surface = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

    def get_image(self, image_path):
        self.image = image_path

    def show_image(self):
        # This is to check if the image is already there
        if self.comparison != self.image:
            if self.image == IMAGE_DEFAULT:
                hold = pygame.image.load(self.image)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, (0,0))
            # clear the area
            else:
                self.display_surface.fill((0,0,0))
                self.comparison = self.image
                # This is to show the new sprite
                hold_request = requests.get(self.image)
                self.image_from_URL = io.BytesIO(hold_request.content)
                hold = pygame.image.load(self.image_from_URL)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, (0,0))
        # If the image is the same go through a standard show 
        else:
            if self.image == IMAGE_DEFAULT:
                hold = pygame.image.load(self.image)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, (0,0))
            else:
                hold_request = requests.get(self.image)
                self.image_from_URL = io.BytesIO(hold_request.content)
                hold = pygame.image.load(self.image_from_URL)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, (0,0))

    def set_position(self):
        # self.position = 
        pass