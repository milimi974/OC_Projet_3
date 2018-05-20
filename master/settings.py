#! /usr/bin/env python3
# coding: utf-8
import os
import pygame

from master.gamepad import GamePad


# Settings constant game screen
# Game screen width size  height size
WIDTH = 1024
HEIGHT = 768
SCREEN_SIZE = (WIDTH, HEIGHT)
GAME_SCREEN_NAME = "MacGyver Escape RoOm" # Game screen name
GAME_SCREEN_BACKGROUND = (0, 0, 0) # Game screen background color
FPS = 60 # Framerate screen

# map settings
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 51, 0)
LIGHTGREY = (100, 100, 100)



# game path
GAME_PATH = os.path.dirname(os.path.dirname(__file__))
ASSET_FOLDER = os.path.join(GAME_PATH, "assets")


# map list in order to draw 0 => map1
MAP_TMX_FILENAME = [
    'map1.tmx',
    'map2.tmx',
]

# player settings
PLAYER_SPEED = 2
PLAYER_ROT_SPEED = 5
PLAYER_MOVE = "smooth" # player movement on screen cell or smooth
PLAYER_SPRITESHEET = "spritesheet/character.png"
PLAYER_TILESIZE = (41, 44)
PLAYER_DIAGONAL_MOVE = True
PLAYER_BOX_COLLISION = pygame.Rect(0, 0, 41, 41)


# camera
CAM_WIDTH = 500
CAM_HEIGHT = 500

DEBUG = True