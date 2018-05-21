#! /usr/bin/env python3
# coding: utf-8
from math import floor

import pygame
from os import path

from master.settings import ASSET_FOLDER, WHITE


class Spritesheet:
    """ this manage spritesheet """

    def __init__(self, filename, tilewidth, tileheight):
        """
        constructor
        :param filename:
        :param cols:
        :param rows:
        """

        self.sheet = pygame.image.load(path.join(ASSET_FOLDER, filename)).convert_alpha()

        self.tilewidth = tilewidth
        self.tileheight = tileheight
        self.rect = self.sheet.get_rect()
        self.cols = floor(self.rect.width / self.tilewidth)
        self.rows = floor(self.rect.height / self.tileheight)
        self.totalCellCount = self.cols * self.rows

        self.cells = [[self.get_image(col*self.tilewidth,row*self.tileheight) for col in range(self.cols)] for row in range(self.rows)]

    def get_image(self, x, y):
        """
        return an image by coordinate
        :param x: int
        :param y: int
        :return: pygame image
        """
        # create a surface for the sheet
        image = pygame.Surface((self.tilewidth, self.tileheight), pygame.SRCALPHA)


        # insert image into surface at position 0,0
        image.blit(self.sheet, (0,0), (x, y, self.tilewidth, self.tileheight))
        return image

    def get_section_image(self, row, col, rows=1, cols=1):
        """
        return a sprite portion image
        :param row: int
        :param col: int
        :param rows: int
        :param cols: int
        :return:
        """
        # create a surface for the sheet
        image = pygame.Surface((cols*self.tilewidth, rows*self.tileheight), pygame.SRCALPHA)
        x = y = 0
        for r in range(row, row+rows):
            for c in range(col, col+cols):
                # insert image into surface at position c,r
                sheet = self.get_image(c*self.tilewidth, r*self.tileheight)
                image.blit(sheet, (x*self.tilewidth, y*self.tileheight), (0, 0, self.tilewidth, self.tileheight))
                x += 1
            x = 0
            y += 1
        return image

    def create_surface(self, row, col, rows, cols):
        """
        create a surface fill with sprite
        :param row: int
        :param col: int
        :param rows: int
        :param cols: int
        :return:
        """
        # create a surface for the sheet
        image = pygame.Surface((cols * self.tilewidth, rows * self.tileheight), pygame.SRCALPHA)
        x = y = 0
        # insert image into surface at position c,r
        sheet = self.get_image(col * self.tilewidth, row * self.tileheight)
        for y in range(rows):
            for x in range(cols):
                image.blit(sheet, (x * self.tilewidth, y * self.tileheight), (0, 0, self.tilewidth, self.tileheight))

        return image

    def get_sprite(self, row, col):
        """
        return an image by cell position
        :param row: int
        :param col: int
        :return:
        """
        return self.cells[row][col]

    def get_animation(self, row, col, size, speed=10):
        """
        return a list of sheet
        :param row: int
        :param col: int
        :param size: int
        :return:
        """
        list_images = []
        for i in range(size):
            list_images.append(self.get_sprite(row, col+i))

        return Animation(list_images, speed)


class Animation:
    """ this manage spritesheet animation """

    def __init__(self, list_images, speed):
        """
        constructor
        :param list_images: list pygame.surface
        :param speed: int speed between image changed
        """
        self.cells = list_images
        # max image in list
        self.max = len(self.cells)
        # current image to return
        self.current = 0
        self.__image = self.cells[self.current]
        self.speed = 0
        self.dt = 100 / speed

    def next(self):
        """ return next image """
        if self.speed > 100:
            self.__image = self.cells[self.current]
            self.current += 1
            if self.current == self.max:
                self.current = 0
            self.speed = 0
        else:
            self.speed += self.dt
    @property
    def image(self):
        # return next image
        self.next()
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image