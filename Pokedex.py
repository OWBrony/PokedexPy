import requests
import pygame
from Display import display 
from Constants import *
from Director import director
from sys import exit

def main():
    runner = director()
    runner.run_game()
    # create the screen

if __name__ == "__main__":
    main()