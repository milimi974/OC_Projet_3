#! /usr/bin/env python3
# coding: utf-8
import pygame

from master.settings import GAME, TILESIZE, BLUE, PLAYER_MOVE, GAMEPAD, PLAYER_SPEED


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

    def move(self, dx=0, dy=0):
        """
        move player to a direction
        :param dx: int
        :param dy: int
        :return:
        """

        self.x += dx
        self.y += dy


    def update(self, dt):

        dx, dy = GAMEPAD.direction
        if PLAYER_MOVE == "cell":
            self.move(dx=dx, dy=dy)
            self.rect.x = self.x * TILESIZE
            self.rect.y = self.y * TILESIZE

        elif PLAYER_MOVE == "smooth":
            dx = dx * PLAYER_SPEED * 100 * dt
            dy = dy * PLAYER_SPEED * 100 * dt
            self.move(dx=dx, dy=dy)
            self.rect.topleft = (self.x, self.y)
