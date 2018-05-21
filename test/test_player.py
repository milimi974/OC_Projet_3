#! /usr/bin/env python3
# coding: utf-8
import sys, os

import pygame as GAME
from pygame.math import Vector2

from master.gamepad import GamePad

GamePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, GamePath)

from master.settings import SCREEN_SIZE, PLAYER_DIAGONAL_MOVE, PLAYER_MOVE
from module.charcater import Player

# pygame initialization
GAME.init()
# create a new window
SCREEN = GAME.display.set_mode(SCREEN_SIZE)
# initialise object manage game time
DT = GAME.time.Clock()


class TestPlayer(object):

    # test if Player instantiate
    def test_player_instantiate(self):
        self.game = GAME
        self.all_sprites = self.game.sprite.LayeredUpdates()
        self.gamepad = GamePad(self,
                               lock_diagonal=PLAYER_DIAGONAL_MOVE,
                               player_move=PLAYER_MOVE)
        player = Player(self, Vector2(10, 15))
        assert player.pos.x == 10
        assert player.pos.y == 15

    # test if player position change
    def test_player_position_change(self):
        self.game = GAME
        self.all_sprites = self.game.sprite.LayeredUpdates()
        self.gamepad = GamePad(self,
                               lock_diagonal=PLAYER_DIAGONAL_MOVE,
                               player_move=PLAYER_MOVE)
        player = Player(self, Vector2(10, 15))
        player.move(1, 2)
        assert player.pos.x == 11
        assert player.pos.y == 17
        player.move(5, 2)
        assert player.pos.x == 16
        assert player.pos.y == 19
        player.move(200, -500)
        assert player.pos.x == 216
        assert player.pos.y == -481