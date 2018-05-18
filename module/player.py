#! /usr/bin/env python3
# coding: utf-8
import pygame

from master.settings import GAME, TILESIZE, BLUE


class Player(pygame.sprite.Sprite):
    """ this manage player """

    def __init__(self, x, y):
        """
        constructor
        :param x: float x position on screen
        :param y: float y position on screen
        """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def update(self, dt):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE