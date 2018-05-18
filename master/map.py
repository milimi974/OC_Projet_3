#! /usr/bin/env python3
# coding: utf-8
from pytmx import pytmx
from pytmx.util_pygame import load_pygame

from master.settings import GAME


class Map():

    # load a map
    def load(self, level):
        """
        load a new map
        :param level:
        :return:
        """


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
        # object contain tile image
        ti = self.tmxdata.get_tile_image_by_id_gid
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
