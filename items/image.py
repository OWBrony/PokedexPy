import pygame
from items.artifact import Artifact
from Constants import *

class Image(Artifact):
    def __init__(self, x=0, y=0):
        self.image = ""
        self.position = ()
        self._x = x
        self._y = y
        self.display_surface = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

    def get_image(self, image_path):
        self.image = image_path

    def show_image(self):
        if self.image == IMAGE_DEFAULT:
            hold = pygame.image.load(self.image)
            picture = pygame.transform.scale(hold, (MAX_WIDTH/2,MAX_HEIGHT/2))
            self.display_surface.blit(picture, (0,0))

    def set_position(self):
        # self.position = 
        pass