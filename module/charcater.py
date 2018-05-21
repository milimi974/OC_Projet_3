#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.math import Vector2

from master.function import collide_hit_rect
from master.settings import TILESIZE, BLUE, PLAYER_MOVE, PLAYER_SPEED, CHARACTER_SPRITESHEET, \
    CHARACTER_TILESIZE, PLAYER_BOX_COLLISION, PLAYER_LAYER, MOB_LAYER
from master.spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    """ this manage player """

    def __init__(self, manager, pos):
        """
        constructor
        :param manager: GameManager
        :param pos: Vector2
        """
        self._layer = PLAYER_LAYER
        self.groups = manager.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = manager

        spritesheet = Spritesheet(CHARACTER_SPRITESHEET,*CHARACTER_TILESIZE)
        self.image = self.idle = spritesheet.get_sprite(1,0)
        self.anim_walk = spritesheet.get_animation(0, 0, 2)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.gamepad = manager.gamepad
        self.rect.center = pos
        self.hit_rect = PLAYER_BOX_COLLISION

    def spawn(self, x, y):
        """
        spawn point position
        :param x:
        :param y:
        :return:
        """

        self.pos = Vector2(x, y)
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

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
        dx, dy = self.gamepad.direction
        if self.gamepad.is_move():

            if PLAYER_MOVE == "cell":
                self.move(dx=dx, dy=dy)
                self.rect.center = self.pos

            elif PLAYER_MOVE == "smooth":
                dx = dx * PLAYER_SPEED * 100 * dt
                dy = dy * PLAYER_SPEED * 100 * dt
                self.move(dx=dx, dy=dy)
                self.rect.center = self.pos
                if pygame.sprite.spritecollideany(self, self.game.walls):
                    self.move(dx=-dx, dy=-dy)
                    self.rect.center = self.pos

            self.image = pygame.transform.rotate(self.anim_walk.image, self.gamepad.rotate)
        else:
            self.image = pygame.transform.rotate(self.idle, self.gamepad.rotate)


class Mob(pygame.sprite.Sprite):
    """ this manage mob """

    def __init__(self, manager, pos):
        """
        constructor
        :param manager: GameManager
        :param pos: Vector2
        """
        self._layer = MOB_LAYER
        self.groups = manager.all_sprites, manager.mob
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = manager

        spritesheet = Spritesheet(CHARACTER_SPRITESHEET,*CHARACTER_TILESIZE)
        self.image = self.idle = spritesheet.get_sprite(3,0)
        self.anim_walk = spritesheet.get_animation(2, 0, 2)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.gamepad = manager.gamepad
        self.rect.center = pos
        

    def spawn(self, x, y):
        """
        spawn point position
        :param x:
        :param y:
        :return:
        """

        self.pos = Vector2(x, y)
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

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
        dx, dy = self.gamepad.direction
        if self.gamepad.is_move():

            if PLAYER_MOVE == "cell":
                self.move(dx=dx, dy=dy)
                self.rect.center = self.pos

            elif PLAYER_MOVE == "smooth":
                dx = dx * PLAYER_SPEED * 100 * dt
                dy = dy * PLAYER_SPEED * 100 * dt
                self.move(dx=dx, dy=dy)
                self.rect.center = self.pos
                if pygame.sprite.spritecollideany(self, self.game.walls):
                    self.move(dx=-dx, dy=-dy)
                    self.rect.center = self.pos

            self.image = pygame.transform.rotate(self.anim_walk.image, self.gamepad.rotate)
        else:
            self.image = pygame.transform.rotate(self.idle, self.gamepad.rotate)