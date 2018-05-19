#! /usr/bin/env python3
# coding: utf-8
import pygame

from master.camera import Camera
from master.gamepad import GamePad
from master.map import Map
from master.settings import SCREEN_SIZE, FPS, GREEN, WIDTH, TILESIZE, LIGHTGREY, HEIGHT, BLACK, \
    PLAYER_MOVE, CAM_HEIGHT, CAM_WIDTH, BLUE, ORANGE, PLAYER_DIAGONAL_MOVE
from module.player import Player


class GameManager():
    """ this class manage game """

    # close game
    close = False



    def __init__(self):
        """ constructor """
        # pygame initialization
        self.game = pygame
        self.game.init()

        # create a new window
        self.screen = self.game.display.set_mode(SCREEN_SIZE)
        # initialise object manage game time
        self.clock = self.game.time.Clock()
        if PLAYER_MOVE == "cell":
            self.game.key.set_repeat(200, 100)
        self.new()

    def new(self):
        """
        initialize new instance for game
        :return:
        """

        # gamepad
        self.gamepad = GamePad(self.game,
                               lock_diagonal=PLAYER_DIAGONAL_MOVE,
                               player_move=PLAYER_MOVE)
        # create a new sprite group
        self.all_sprites = self.game.sprite.Group()

        # init map
        self.map = Map()
        self.player = Player(self, 0, 0)

        # collide object
        for tile_object  in self.map.tmxdata.objects:
            pass
        # camera
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        """ run game """
        # update clock game time by frame rate
        dt = self.clock.tick(FPS) / 1000
        self.events()
        self.update(dt)
        self.draw()

    def update(self, dt):
        """ update module
        Keyword arguments:
        dt -- integer Delta time time between 2 update Main Loop

        """

        self.all_sprites.update(dt)
        self.camera.update(self.player)

    def draw(self):
        """ draw module """
        # clear window
        self.screen.fill(BLACK)
        #self.draw_grid()
        # draw map
        self.screen.blit(self.map.map_img, self.camera.apply_rect(self.map.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # self.all_sprites.draw(self.screen)
        # drawing everything, flip the display
        self.game.display.flip()

    def draw_grid(self):
        """ draw a grid """
        for x in range(0, WIDTH, TILESIZE):
            self.game.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, TILESIZE):
            self.game.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def events(self):
        """
        manage game events
        :return:
        """
        # process input (events)
        self.gamepad.hook_events()

        # if user close the game
        if self.gamepad.close :
            self.close = True

    def quit(self):
        """ leaved the game """
        self.game.quit()
