import pygame
import sys
from Constants import *

class text_box():
    def __init__(self, display):
        self.screen = display
        self.clock = pygame.time.Clock()
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ""
        self.input_box = pygame.Rect(20, 300, 100, 32)
        self.active
        pass