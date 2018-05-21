#! /usr/bin/env python3
# coding: utf-8
from os import path

import pygame
from pygame.math import Vector2
from pytmx import pytmx
from pytmx.util_pygame import load_pygame

from master.settings import MAP_TMX_FILENAME, ASSET_FOLDER, ITEMS_LAYER, WALL_LAYER


class TileMap:
    """ this manage map format tmx """

    def __init__(self, game):
        """
        constructor
        :param game: Gamemanager
        """
        self.game = game

    def new(self, filename):
        """
        initialize
        :param filename: string
        """
        # load tmx file for pygame with surface
        tm = load_pygame(filename, pixelalpha=True)
        # define sizes
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        # get tmx object
        self.tmxdata = tm
        # items object

    def render(self, surface):
        """
        draw map element
        :param surface: object pygame screen
        :return:
        """
        # create a short method name
        ti = self.tmxdata.get_tile_image_by_gid
        # loop of all visible layers
        for layer in self.tmxdata.visible_layers:
            if not layer.name == "items":
                # if layer are a tile layer
                if isinstance(layer, pytmx.TiledTileLayer):
                    # get position and tile id
                    for x, y, gid in layer:
                        # get tile image
                        tile = ti(gid)
                        # if tile exist
                        if tile:
                            # draw tile
                            surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                y * self.tmxdata.tileheight))

    def make_map(self):
        """ return a surface width map draw in """

        # create a surface to draw the map
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # draw the map
        self.render(temp_surface)
        return temp_surface

    def get_items_layer(self):
        """ return item layer """
        return self.tmxdata.get_layer_by_name("items")

class Item(pygame.sprite.Sprite):
    """ this manage item """

    def __init__(self, game, pos, image, type):
        """
        constructor
        :param game: GameManager
        :param pos: tuple x,y
        :param type: string
        """
        self._layer = ITEMS_LAYER
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Obstacle(pygame.sprite.Sprite):
    """ this manage wall """

    def __init__(self, game, x, y, w, h):
        """
        constructor
        :param game: GameManager
        :param x: int
        :param y: int
        :param w: int
        :param h: int
        """
        self._layer = WALL_LAYER
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class Map(TileMap):
    """ this manage map """

    def __init__(self, game):
        """ constructor """
        super().__init__(game)
        # init first map
        self.current_map = int(0)
        # init map list
        self.maps_tmx = MAP_TMX_FILENAME

        # load first map
        self.load()

    # load a map
    def load(self, level=0):
        """
        load a new map
        :param level: int
        :return:
        """

        # if level exist
        if self.maps_tmx[int(level)]:
            filename = path.join(path.join(ASSET_FOLDER, 'maps'), self.maps_tmx[level])
            self.new(filename)
            self.map_img = self.make_map()
            self.map_rect = self.map_img.get_rect()

