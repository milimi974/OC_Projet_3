#! /usr/bin/env python3
# coding: utf-8
from master.settings import GAME, SCREEN_SIZE, FPS, GREEN


class GameManager():
    """ class manage game """

    # close game
    close = False
    # create a new sprite group
    all_sprites = GAME.sprite.Group()


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
        # update clock game time by frame rate
        self.clock.tick(FPS)

        self.update(self.clock.get_time())
        self.draw()

    def update(self, dt):
        """ update module
        Keyword arguments:
        dt -- integer Delta time time between 2 update Main Loop

        """
        self.all_sprites.update(dt)

    def draw(self):
        """ draw module """
        # clear window
        self.screen.fill(GREEN)
        self.all_sprites.draw(self.screen)
        # drawing everything, flip the display
        GAME.display.flip()

    def quit(self):
        GAME.quit()