import pygame
import sys
from Constants import *

class text_box():
    def __init__(self, display):
        pygame.init()
        self.screen = display
        self.clock = pygame.time.Clock()
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ""
        self.input_box = pygame.Rect(20, 300, 100, 32)
        self.active = False
        self.color_passive = pygame.Color(242,242,242)
        self.color_active = pygame.Color(255,255,255)
        self.color = self.color_passive
    
    def select_color(self):
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.input_box)