#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.math import Vector2

from master.function import collide_hit_rect
from master.settings import TILESIZE, BLUE, PLAYER_MOVE, PLAYER_SPEED, CHARACTER_SPRITESHEET, \
    CHARACTER_TILESIZE, PLAYER_BOX_COLLISION, PLAYER_LAYER, MOB_LAYER, MOB_MOVE, MOB_SPEED, PLAYER_HEALTH
from master.spritesheet import Spritesheet
import random


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
        self.health = PLAYER_HEALTH

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

    def __init__(self, manager, pos, type, name):
        """
        constructor
        :param manager: GameManager
        :param pos: Vector2
        """
        self._layer = MOB_LAYER
        self.groups = manager.all_sprites, manager.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = manager

        self.sprite(type)
        self.__rotate = -180
        self.rect = self.image.get_rect()
        self.pos = pos
        self.type = type
        self.name = name
        self.gamepad = manager.gamepad
        self.rect.center = pos
        self.follow = False


    def sprite(self, type):
        """
        load mob type
        :param type:
        :return:
        """
        spritesheet = Spritesheet(CHARACTER_SPRITESHEET, *CHARACTER_TILESIZE)
        if type == "boss":
            self.image = self.idle = spritesheet.get_sprite(5, 0)
            self.anim_walk = spritesheet.get_animation(4, 0, 2, 15)
        else:
            self.image = self.idle = spritesheet.get_sprite(3, 0)
            self.anim_walk = spritesheet.get_animation(2, 0, 2, 15)

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

        if self.is_aggro():
            dx, dy = self.get_direction()
            self.look_at()
            if MOB_MOVE == "smooth":
                dx = dx * MOB_SPEED * 100 * dt
                dy = dy * MOB_SPEED * 100 * dt

            self.move(dx=dx, dy=dy)
            self.rect.center = self.pos
            if pygame.sprite.spritecollideany(self, self.game.walls):
                self.move(dx=-dx, dy=-dy)
                self.rect.center = self.pos

            self.image = pygame.transform.rotate(self.anim_walk.image, self.__rotate)
        else:
            self.image = pygame.transform.rotate(self.idle, self.__rotate)

    def is_aggro(self):
        """ follow player if in range """
        px, py = self.game.player.pos
        mx, my = self.pos
        x = abs(px - mx)
        y = abs(py - my)

        if self.follow and x < 256 and y < 256:
           if random.random() < 0.002:
               random.choice(self.game.zombie_roar).play()
           return True
        else:
            if x < 128 and y < 128:
                self.follow = True
                return True
            self.follow = False
            return False

    def look_at(self):
        """
        turn mob in direction
        :param dx:
        :param dy:
        :return:
        """
        self.__rotate = (self.game.player.pos - self.pos).angle_to(Vector2(1, 0))

    def get_direction(self):
        """ defined player position """
        px, py = self.game.player.pos
        mx, my = self.pos


        dx = 0
        dy = 0

        if px < mx :
            dx = -1
        elif px > mx:
            dx = 1

        if py < my:
            dy = -1
        elif py > my:
            dy = 1

        # if mob and player align
        if px == mx :
            dy = 0
        elif py == my:
            dx = 0

        # random direction if dx and dy not equal 0
        if not dx == 0 and not dy == 0:
            r = random.randint(1,101)
            if r < 49 :
                dx = 0
            else:
                dy = 0

        return (dx, dy)
