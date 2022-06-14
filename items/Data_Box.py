from API_Calling.API_Call import *
from items.image import *
from Constants import *

class data_box():
    def __init__(self, display):
        pygame.init()
        self.screen = display
        self.has_stat = False
        self.has_ability = False
        self.pokemon_name = None
        self.name = None
        # A list to hold the stats passed in
        self.stat = None
        # A list to hold the abilities passed in
        self.ability = None
        # This is to hold the position tuple passed in
        self.position = None
        self._text_stat = f"{self.name}: {self.stat}"
        self._text_ability = f"{self.name}: {self.ability}"
        self._text_pokemon_name = f"Name: {self.pokemon_name}"
        # Clock for refresh
        self.clock = pygame.time.Clock()
        # Sets the font
        self.base_font = pygame.font.Font(None, 24)
        # set the color of the box background
        self.color = (64,64,64)
        # This is the display surface. DO NOT DELETE
        self.display = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

    def draw_rect(self,screen):
        self.rectangle = pygame.draw.rect(self.display, self.color, self.position)

    def set_position(self,right,top,length,thickness):
        location = (right,top,length,thickness)
        self.position = location

    def show_text(self):
        if self.has_stat:
            text_surface = self.base_font.render(self._text_stat, True, (255,255,255))
            self.display.blit(text_surface, self.rectangle)
            pygame.display.update()
        elif self.ability:
            text_surface = self.base_font.render(self._text_ability, True, (255,255,255))
            self.display.blit(text_surface, self.rectangle)
            pygame.display.update()
        else:
            text_surface = self.base_font.render(self._text_pokemon_name, True, (255,255,255))
            self.display.blit(text_surface, self.rectangle)
            pygame.display.update()
            
    def recieve_data(self, name, ability = False, stat = None):
        if stat:
            self.has_stat = True
            self.stat = stat
            self.name = name
        elif ability:
            self.has_ability = True
            self.name = name
        else:
            self.pokemon_name = name
