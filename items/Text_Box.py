import pygame
import sys
from Constants import *

class text_box():
    def __init__(self, display):
        pygame.init()
        # The imported screen
        # self.screen = display
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
        self._input_box = (80, 425, 250, 32)
        # Flag for deciding the color
        self.active = False
        # set the color
        self.color_passive = pygame.Color(142,142,142)
        self.color_active = pygame.Color(255,255,255)
        self.color = self.color_passive
        # This is the display surface. DO NOT DELETE
        self.display = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
        # to hold the rectangle
        self.rectangle = None
        # self.text_surface = None 
    
    def select_color(self):
        """This should set the color of the text bar
        based on whether it is active or not."""
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

    def draw_rect(self,screen):
        self.rectangle = pygame.draw.rect(self.display, self.color, self._input_box)

    def show_text(self):
        text_surface = self.base_font.render(self.user_text, True, (0,0,0))
        self.display.blit(text_surface, self.rectangle)
        pygame.display.update()

    def clear_text(self):
        self.user_text = ""
    
    # def update_rect(self):
    #     self.screen.update()

    # def collide_point(self,position):
    #     x,y = position.split(",")
    #     if self.rectangle.collidepoint(x,y):
    #         return True
    #     else:
    #         return False

