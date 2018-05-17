#! /usr/bin/env python3
# coding: utf-8
import os
import pygame


MAP_COLUMN = 15 # Grid column size
MAP_ROW = 15 # Grid row size
CELL_WIDTH = 21 # Grid cell Width
CELL_HEIGHT = 21 # Grid cell Height
MAP_ITEMS = ["5", "6", "7"] # Lis of items ID
ITEMS_SPACE = 2 # Distance between items



# Settings constant game screen
# Game screen width size  height size
WIDTH = 320
HEIGHT = 320
SCREEN_SIZE = (WIDTH, HEIGHT)
GAME_SCREEN_NAME = "MacGyver Escape RoOm" # Game screen name
GAME_SCREEN_BACKGROUND = (0, 0, 0) # Game screen background color
FPS = 24 # Framerate screen

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

GAME = pygame

# game path
GAME_PATH = os.path.dirname(__file__)
ASSET_FOLDER = os.path.join(GAME_PATH, "assets")