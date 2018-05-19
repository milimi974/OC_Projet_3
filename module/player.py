#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.math import Vector2

from master.settings import TILESIZE, BLUE, PLAYER_MOVE, PLAYER_SPEED, PLAYER_SPRITESHEET, \
    PLAYER_TILESIZE
from master.spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    """ this manage player """

    def __init__(self, manager, x, y):
        """
        constructor
        :param manager: GameManager
        :param x: float x position on screen
        :param y: float y position on screen
        """
        self.groups = manager.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        spritesheet = Spritesheet(PLAYER_SPRITESHEET,*PLAYER_TILESIZE)
        self.image = self.idle = spritesheet.get_sprite(1,0)
        self.anim_walk = spritesheet.get_animation(0, 0, 2)
        self.rect = self.image.get_rect()
        self.pos = Vector2(x, y)
        self.gamepad = manager.gamepad



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
        if self.gamepad.is_move():
            dx, dy = self.gamepad.direction
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

            self.image = pygame.transform.rotate(self.anim_walk.image, self.gamepad.rotate)
        else:
            self.image = pygame.transform.rotate(self.idle, self.gamepad.rotate)
