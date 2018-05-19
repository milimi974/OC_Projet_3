#! /usr/bin/env python3
# coding: utf-8
import sys, os
GamePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, GamePath)

from master.map import Map
from master.settings import  SCREEN_SIZE
import pygame as GAME
# pygame initialization
GAME.init()
# create a new window
SCREEN = GAME.display.set_mode(SCREEN_SIZE)
# initialise object manage game time
DT = GAME.time.Clock()


class TestMap(object):

    # test if loading map tmx
    def test_loading_map_tmx(self):
        map = Map()
        assert map.maps_tmx[0] == 'map1.tmx'
        assert map.maps_tmx[1] == 'map2.tmx'

    # test if drawing map on screen
    def test_drawing_map_screen(self):
        map = Map()
        assert SCREEN.blit(map.map_img, map.map_rect)
