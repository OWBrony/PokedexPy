import pygame
import sys
from Constants import *

class text_box():
    def __init__(self, display):
        pygame.init()
        # The imported screen
        self.screen = display
        # Clock for refresh
        self.clock = pygame.time.Clock()
        # Sets the font
        self.base_font = pygame.font.Font(None, 32)
        # To set the text in the text box
        self.user_text = ""
        # To set the size of the box
        # First value: How far to the right
        # Second value: How far from the top
        # Third value: How long the box will be
        # Fourth value: How thick the box will be
        self.input_box = (80, 425, 250, 32)
        # Flag for deciding the color
        self.active = False
        # set the color
        self.color_passive = pygame.Color(142,142,142)
        self.color_active = pygame.Color(255,255,255)
        self.color = self.color_passive
        # Don't know why I need a second screen but it is here.
        self.display = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
        # to hold the rectangle
        self.rectangle = None
    
    def select_color(self):
        """This should set the color of the text bar
        based on whether it is active or not."""
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

    def draw_rect(self,screen):
        self.rectangle = pygame.draw.rect(self.display, self.color, self.input_box)
        # self.display.blit(self.display, (400,20))

    def collide_point(self,position):
        if self.rectangle.collidepoint((position)):
            return True
        else:
            return False

