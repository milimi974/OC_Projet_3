#! /usr/bin/env python3
# coding: utf-8
from os import path
from pytmx import pytmx
from pytmx.util_pygame import load_pygame

from master.settings import GAME, MAP_TMX_FILENAME, ASSET_FOLDER


class Map():
    """ this manage map """
    def __init__(self):
        """ constructor """
        # init first map
        self.current_map = 0
        # init map list
        self.maps_tmx = MAP_TMX_FILENAME
        # map container
        self.map = False

        # load first map
        self.load(self.current_map)

    # load a map
    def load(self, level):
        """
        load a new map
        :param level:
        :return:
        """
        # if level exist
        if self.maps_tmx[level]:
            filename = path.join(path.join(ASSET_FOLDER, 'maps'), self.maps_tmx[level])
            self.map = TileMap(filename)
            self.map_img = self.map.make_map()
            self.map_rect = self.map_img.get_rect()

class TileMap:
    """ this manage map format tmx """

    def __init__(self, filename):
        """
        constructor
        :param filename: string
        """

        # load tmx file for pygame with surface
        tm = load_pygame(filename, pixelalpha=True)
        # define sizes
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        # get tmx object
        self.tmxdata = tm

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
        temp_surface = GAME.Surface((self.width, self.height))
        # draw the map
        self.render(temp_surface)
        return temp_surface


class Wall:
    """ this manage wall """

    def render(self):
        """ render """
        pass

