#! /usr/bin/env python3
# coding: utf-8
import math
import pygame
from pygame.math import Vector2

from master.camera import Camera
from master.gamepad import GamePad
from master.gui import Gui
from module.map import Map, Obstacle, Item
from master.settings import SCREEN_SIZE, FPS, WIDTH, TILESIZE, LIGHTGREY, HEIGHT, BLACK, \
    PLAYER_MOVE, PLAYER_DIAGONAL_MOVE, DEBUG, CYAN
from module.charcater import Player


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
        self.all_sprites = self.game.sprite.LayeredUpdates()
        self.walls = self.game.sprite.Group()
        self.items = self.game.sprite.Group()
        self.mobs = self.game.sprite.Group()

        # init map
        self.map = Map(self)

        # camera
        self.camera = Camera(self.map.width, self.map.height)

        # init gui
        args = {
            'width': WIDTH,
            'height': 64,
            'x': 0,
            'y': 0,
        }
        self.gui = Gui(self)

        # self.player = Player(self, 0, 0)
        layer = self.map.get_items_layer()
        tmxdata = self.map.tmxdata
        # collide object
        for tile_object  in tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, self.object_tmx_center(tile_object))

            if tile_object.name == 'item':
                object_pos = self.object_tmx_position(tile_object, tmxdata.tilewidth, tmxdata.tileheight)
                for x, y, image in layer.tiles():
                    tile_pos = (x*tmxdata.tilewidth, y*tmxdata.tileheight)
                    if object_pos == tile_pos:
                        Item(self, self.object_tmx_center(tile_object), image, tile_object.type)

            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

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

    def object_tmx_center(self, object):
        """
        return position of object tmx center
        :param object: tmx
        :return:
        """
        x = object.x + (object.width / 2)
        y = object.y + (object.height / 2)
        return Vector2(x, y)

    def object_tmx_position(self, object, tilewidth, tileheight):
        """
        return position of object tmx x y
        :param object: tmx
        :return:
        """
        x = math.floor(object.x / tilewidth ) * tilewidth
        y = math.floor(object.y / tilewidth ) * tileheight
        return (x, y)

    def draw(self):
        """ draw module """
        # clear window
        self.screen.fill(BLACK)

        # draw map
        self.screen.blit(self.map.map_img, self.camera.apply_rect(self.map.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if DEBUG:
               pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.rect), 1)

        if DEBUG:
            for sprite in self.walls:
               pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.rect), 1)

        self.draw_grid()

        # draw gui
        self.gui.draw(self.screen)

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
