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

    # test if player position change
    def test_player_position_change(self):
        player = Player(10, 15)
        player.move(1, 2)
        assert player.x == 11
        assert player.y == 17
        player.move(5, 2)
        assert player.x == 16
        assert player.y == 19
        player.move(200, -500)
        assert player.x == 216
        assert player.y == -481