#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.math import Vector2

from master.settings import GAME, TILESIZE, BLUE, PLAYER_MOVE, GAMEPAD, PLAYER_SPEED, PLAYER_SPRITESHEET, \
    PLAYER_TILESIZE
from master.spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    """ this manage player """

    def __init__(self, x, y):
        """
        constructor
        :param x: float x position on screen
        :param y: float y position on screen
        """
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet(PLAYER_SPRITESHEET,*PLAYER_TILESIZE)
        self.image = self.idle = spritesheet.get_sprite(1,0)
        self.anim_walk = spritesheet.get_animation(0, 0, 2)
        self.rect = self.image.get_rect()
        self.pos = Vector2(x, y)


    def move(self, dx=0, dy=0):
        """
        move player to a direction
        :param dx: int
        :param dy: int
        :return:
        """

        self.pos.x += dx
        self.pos.y += dy


    def update(self, dt):
        if GAMEPAD.is_move():
            dx, dy = GAMEPAD.direction
            if PLAYER_MOVE == "cell":
                self.move(dx=dx, dy=dy)
                self.pos * TILESIZE
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y

            elif PLAYER_MOVE == "smooth":
                dx = dx * PLAYER_SPEED * 100 * dt
                dy = dy * PLAYER_SPEED * 100 * dt
                self.move(dx=dx, dy=dy)
                self.rect.topleft = (self.pos.x, self.pos.y)

            self.image = self.anim_walk.image
        else:
            self.image = self.idle