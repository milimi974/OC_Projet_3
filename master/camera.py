#! /usr/bin/env python3
# coding: utf-8
import pygame

from master.settings import WIDTH, HEIGHT


class Camera:
    """ this manage camera """

    def __init__(self, width, height):
        """
        constructor
        :param width: int
        :param height: int
        """
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        """ apply offset to object """
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        """ apply offset to rect"""
        return rect.move(self.camera.topleft)

    def update(self, target):
        """
        this update camera position
        :param target: entity to follow
        :return:
        """
        if target:
            x = -target.rect.x + int(WIDTH / 2)
            y = -target.rect.y + int(HEIGHT / 2)
            self.camera = pygame.Rect(x, y, self.width, self.height)