from API_Calling.API_Call import *
from items.image import *
from Constants import *

class data_box():
    def __init__(self, display):
        self.has_data = False
        # A list to hold the stats passed in
        self.stats = None
        # A list to hold the abilities passed in
        self.abilities = None
        # This is to hold the position tuple passed in
        self.position = None
        # Clock for refresh
        self.clock = pygame.time.Clock()
        # Sets the font
        self.base_font = pygame.font.Font(None, 24)
        # set th ecolor of the box background
        self.color = (124,124,124)
        # This is the display surface. DO NOT DELETE
        self.display = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

    def draw_rect(self,screen):
        self.rectangle = pygame.draw.rect(self.display, self.color, self._input_box)

    def show_text(self):
        text_surface = self.base_font.render(self.user_text, True, (0,0,0))
        self.display.blit(text_surface, self.rectangle)
        pygame.display.update()

