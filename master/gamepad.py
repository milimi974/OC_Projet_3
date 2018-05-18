#! /usr/bin/env python3
# coding: utf-8

# class manage interaction with keyboard and pygame screen
import pygame



class GamePad():

    def __init__(self, game):
        self.mouse_position = (0, 0)
        self.__direction = (0, 0)
        self.key_states = {}
        self.game = game
        self.close = False


    def is_key(self, keyname):
        """
        return if a key is pressed
        :param keyname: string
        :return:
        """
        return self.key_states[keyname]

    # return direction move
    @property
    def direction(self):
        return self.__direction

    # direction setter
    @direction.setter
    def direction(self, dir):
        self.__direction = dir

    def hook_events(self):
        """ save keypress event """
        for event in self.game.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.close = True

        # get all key pressed
        self.key_states = self.game.key.get_pressed()
        dx, dy = (0, 0)
        if self.key_states[pygame.K_LEFT]:
            dx = -1
        if self.key_states[pygame.K_RIGHT]:
            dx = 1
        if self.key_states[pygame.K_UP]:
            dy = -1
        if self.key_states[pygame.K_DOWN]:
            dy = 1

        self.direction = (dx, dy)


