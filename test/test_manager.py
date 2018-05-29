#! /usr/bin/env python3
# coding: utf-8
import sys, os


GamePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, GamePath)

from master.manager import GameManager
from module.charcater import Player


class TestGameManager(object):

    # test if game manager create items first map 8
    def test_game_create_item(self):
        GAME = GameManager()
        GAME.run()
        GAME.start = True
        assert len(GAME.items) == 8

    # test if game manager create player
    def test_game_create_player(self):
        GAME = GameManager()
        GAME.run()
        GAME.start = True
        assert isinstance(GAME.player, Player)


    # test if game manager change map
    def test_game_change_map(self):
        GAME = GameManager()
        GAME.run()
        GAME.start = True
        GAME.next()
        assert GAME.map.current_map == 2
