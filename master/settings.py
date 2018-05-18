#! /usr/bin/env python3
# coding: utf-8
import os
import pygame

from master.gamepad import GamePad

MAP_COLUMN = 15 # Grid column size
MAP_ROW = 15 # Grid row size
MAP_ITEMS = ["5", "6", "7"] # Lis of items ID
ITEMS_SPACE = 2 # Distance between items




# Settings constant game screen
# Game screen width size  height size
WIDTH = 1024
HEIGHT = 768
SCREEN_SIZE = (WIDTH, HEIGHT)
GAME_SCREEN_NAME = "MacGyver Escape RoOm" # Game screen name
GAME_SCREEN_BACKGROUND = (0, 0, 0) # Game screen background color
FPS = 60 # Framerate screen

# map settings
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHTGREY = (100, 100, 100)

GAME = pygame


# game path
GAME_PATH = os.path.dirname(os.path.dirname(__file__))
ASSET_FOLDER = os.path.join(GAME_PATH, "assets")


# map list in order to draw 0 => map1
MAP_TMX_FILENAME = [
    'map1.tmx',
    'map2.tmx',
]

# player settings
PLAYER_SPEED = 5
PLAYER_MOVE = "cell" # player movement on screen cell or smooth

# gamepad
GAMEPAD = GamePad(GAME, lock_diagonal=True, player_move=PLAYER_MOVE)