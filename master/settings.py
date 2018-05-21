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
GREEN = (102, 255, 102)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 204, 0)
ORANGE = (255, 102, 0)
LIGHTGREY = (100, 100, 100)



# game path
GAME_PATH = os.path.dirname(os.path.dirname(__file__))
ASSET_FOLDER = os.path.join(GAME_PATH, "assets")
SOUNDS = os.path.join(ASSET_FOLDER, "sounds")
MUSICS = os.path.join(ASSET_FOLDER, "musics")


# map list in order to draw 0 => map1
MAP_TMX_FILENAME = [
    'map1.tmx',
    'map2.tmx',
]
# spritesheet
CHARACTER_SPRITESHEET = "spritesheet/character.png"
CHARACTER_TILESIZE = (41, 44)
GUI_SPRITESHEET =  "spritesheet/gui.png"

# player settings
PLAYER_SPEED = 2
PLAYER_ROT_SPEED = 5
PLAYER_MOVE = "smooth" # player movement on screen cell or smooth
PLAYER_DIAGONAL_MOVE = True
PLAYER_BOX_COLLISION = pygame.Rect(0, 0, 41, 41)
PLAYER_HEALTH = 200

# mob
MOB_SPEED = 1.6
MOB_ROT_SPEED = 5
MOB_MOVE = "cell" # player movement on screen cell or smooth
MOB_DIAGONAL_MOVE = True
MOB_BOX_COLLISION = pygame.Rect(0, 0, 41, 41)
MOB_DAMAGE = 1

# layers

PLAYER_LAYER = 2
MOB_LAYER = 3
ITEMS_LAYER = 1
WALL_LAYER = 1
GUI_LAYER = 9

# camera
CAM_WIDTH = 500
CAM_HEIGHT = 500

# sounds
BG_MUSIC = 'main.ogg'
MOB_MOAN_SOUNDS = ['zombie-roar.wav','zombie-roar-2.wav']
MOB_HIT_SOUNDS = ['player_pain']
EFFECTS_SOUNDS = {'level_start': 'level.wav',
                  'death': 'death.wav',
                  'health_up': 'pick-up-health.wav',
                  'hit': 'slap.wav',
                  'item_pickup': 'item-pickup.ogg',
                  }



DEBUG = True

