#! /usr/bin/env python3
# coding: utf-8
from master.settings import GAME, SCREEN_SIZE


class GameManager():
    """ class manage game """
    close = False

    def __init__(self):
        """ constructor """
        # pygame initialization
        GAME.init()
        # create a new window
        self.screen = GAME.display.set_mode(SCREEN_SIZE)
        # initialise object manage game time
        self.clock = GAME.time.Clock()


    def run(self):
        """ run game """
        pass

    def quit(self):
        GAME.quit()