import pygame
from services.Display import display 
from Constants import *
from items.artifact import Artifact
from items.image import Image
from items.Text_Box import text_box
from scroll_bar import scroller
from resources.kanto_dex import *
from items.Data_Box import *
class director:
    
    def __init__(self):
        """Creates new instance of director"""
        self._video_service = display()
        self.run = True

    # def set_position(self, right):

    def run_game(self):
        # First value: How far to the right
        # Second value: How far from the top
        # Third value: How long the box will be
        # Fourth value: How thick the box will be
        data_box_top = 0
        data_box_right = MAX_WIDTH / 2 + 10
        data_box_length = MAX_WIDTH
        data_box_thick = 24
        # This is to set the position of data boxes
        data_box_position = (data_box_right, data_box_top, data_box_length, data_box_thick)
        # This is to set up the databoxes for the pokemon info
        name_box = data_box(self._video_service)
        first_ability_box = data_box(self._video_service)
        second_ability_box = data_box(self._video_service)
        hidden_ability_box = data_box(self._video_service)
        hp_box = data_box(self._video_service)
        attack_box = data_box(self._video_service)
        defence_box = data_box(self._video_service)
        spec_attack_box = data_box(self._video_service)
        spec_defence_box = data_box(self._video_service)
        speed_box = data_box(self._video_service)
        # This is to set the positions
        name_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        first_ability_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        second_ability_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        hidden_ability_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        hp_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        attack_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        defence_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        spec_attack_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        spec_defence_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        data_box_top += 25
        speed_box.set_position(data_box_right, data_box_top, data_box_length, data_box_thick)
        # This is the API call object that I will use later
        database_call = Caller()
        clock = pygame.time.Clock()
        run = True
        # this is to set the current pokemon's image.
        current_pokemon_image = Image()
        # This is to set the default for the window opening.
        current_pokemon_image.get_image(IMAGE_DEFAULT)
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
                    if text_bar.rectangle.collidepoint(pygame.mouse.get_pos()):
                        text_bar.active = True
                        text_bar.select_color()
                    else:
                        text_bar.active = False
                        text_bar.select_color()
                # This is to check if a key was pressed.
                if event.type == pygame.KEYDOWN and text_bar.active == True:
                    # if backspace remove a letter
                    if event.key == pygame.K_BACKSPACE:
                        text_bar.user_text = text_bar.user_text[:-1]
                        # text_bar.show_text()
                    elif event.key == pygame.K_RETURN:
                        database_call.get_data(text_bar.user_text)
                        current_pokemon_image.get_image(database_call.sprite)
                        name_box.recieve_data(database_call.pokemon_name)
                        first_ability_box.recieve_data(database_call.first_ability)
                        if database_call.second_ability:
                            second_ability_box.recieve_data(database_call.second_ability,True)
                        else:
                            second_ability_box.recieve_data("None", True)
                        if database_call.hidden_ability:
                            hidden_ability_box.recieve_data(database_call.hidden_ability,True)
                        else:
                            hidden_ability_box.recieve_data("None", True)
                        hp_box.recieve_data("Health: ",False,database_call.health)
                        attack_box.recieve_data("Attack: ",False,database_call.attack)
                        defence_box.recieve_data("Defence: ",False,database_call.defense)
                        spec_attack_box.recieve_data("Special Attack: ",False,database_call.spec_attack)
                        spec_defence_box.recieve_data("Special Defence: ",False,database_call.spec_defense)
                        speed_box.recieve_data("Speed: ",False,database_call.speed)

                        text_bar.clear_text()
                        text_bar.active = False
                        text_bar.select_color()
                        self._video_service.clear_window()
                    else:
                        text_bar.user_text += event.unicode
                        # text_bar.show_text()
                        # print(text_bar.user_text)
            # Show the image and info
            text_bar.draw_rect(self._video_service)
            text_bar.show_text()
            if name_box.pokemon_name:
                name_box.draw_rect(self._video_service)
                name_box.show_text()
            if first_ability_box.has_ability:
                first_ability_box.draw_rect(self._video_service)
                first_ability_box.show_text()
            if second_ability_box.has_ability:
                second_ability_box.draw_rect(self._video_service)
                second_ability_box.show_text()
            if hidden_ability_box.has_ability:
                hidden_ability_box.draw_rect(self._video_service)
                hidden_ability_box.show_text()
            if hp_box.has_stat:
                hp_box.draw_rect(self._video_service)
                hp_box.show_text()
            if attack_box.has_stat:
                attack_box.draw_rect(self._video_service)
                attack_box.show_text()
            if defence_box.has_stat:
                defence_box.draw_rect(self._video_service)
                defence_box.show_text()
            if spec_attack_box.has_stat:
                spec_attack_box.draw_rect(self._video_service)
                spec_attack_box.show_text()
            if spec_defence_box.has_stat:
                spec_defence_box.draw_rect(self._video_service)
                spec_defence_box.show_text()
            if speed_box.has_stat:
                speed_box.draw_rect(self._video_service)
                speed_box.show_text()
            # This is to display the image that was chosen
            current_pokemon_image.show_image()
            
            # this is to hopefully refresh the screen
            self._video_service.clear_buffer()
            # self._video_service.update()
            clock.tick(60)
        self._video_service.close_window()