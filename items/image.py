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
        self.position = (0,0,MAX_WIDTH/2,MAX_HEIGHT/2)
        self.rectangle = None
        self._x = x
        self._y = y
        self.display_surface = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

    def draw_rect(self,screen):
        self.rectangle = pygame.draw.rect(self.display_surface, (255,255,255), self.position)

    def get_image(self, image_path):
        self.image = image_path

    def show_image(self):
        # This is to check if the image is already there
        if self.comparison != self.image:
            if self.image == IMAGE_DEFAULT:
                hold = pygame.image.load(self.image)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, self.rectangle)
            # clear the area
            else:
                self.display_surface.fill((255,255,255),self.rectangle)
                self.comparison = self.image
                # This is to show the new sprite
                hold_request = requests.get(self.image)
                self.image_from_URL = io.BytesIO(hold_request.content)
                hold = pygame.image.load(self.image_from_URL)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, self.rectangle)
        # If the image is the same go through a standard show 
        else:
            if self.image == IMAGE_DEFAULT:
                hold = pygame.image.load(self.image)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, self.rectangle)
            else:
                hold_request = requests.get(self.image)
                self.image_from_URL = io.BytesIO(hold_request.content)
                hold = pygame.image.load(self.image_from_URL)
                picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
                self.display_surface.blit(picture, self.rectangle)

    def set_position(self):
        # self.position = 
        pass