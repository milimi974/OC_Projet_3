#! /usr/bin/env python3
# coding: utf-8
import sys, os



GamePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, GamePath)

from master.settings import GAME, SCREEN_SIZE
from module.player import Player

# pygame initialization
GAME.init()
# create a new window
SCREEN = GAME.display.set_mode(SCREEN_SIZE)
# initialise object manage game time
DT = GAME.time.Clock()


class TestPlayer(object):

    # test if Player instantiate
    def test_player_instantiate(self):
        player = Player(10, 15)
        assert player.x == 10
        assert player.y == 15

