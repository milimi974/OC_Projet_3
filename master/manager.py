#! /usr/bin/env python3
# coding: utf-8
from master.map import Map
from master.settings import GAME, SCREEN_SIZE, FPS, GREEN, WIDTH, TILESIZE, LIGHTGREY, HEIGHT
from module.player import Player


class GameManager():
    """ class manage game """

    # close game
    close = False



    def __init__(self):
        """ constructor """
        # pygame initialization
        GAME.init()
        # create a new window
        self.screen = GAME.display.set_mode(SCREEN_SIZE)
        # initialise object manage game time
        self.clock = GAME.time.Clock()
        self.new()

    def new(self):
        # initialize new instance for game
        # create a new sprite group
        self.all_sprites = GAME.sprite.Group()

        # init map
        self.map = Map()
        self.player = Player(0, 0)
        self.all_sprites.add(self.player)

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
        # self.screen.fill(GREEN)
        self.draw_grid()
        # draw map
        #self.screen.blit(self.map.map_img, self.map.map_rect)
        self.all_sprites.draw(self.screen)
        # drawing everything, flip the display
        GAME.display.flip()

    def draw_grid(self):
        """ draw a grid """
        for x in range(0, WIDTH, TILESIZE):
            GAME.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, TILESIZE):
            GAME.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def quit(self):
        GAME.quit()