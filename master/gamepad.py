#! /usr/bin/env python3
# coding: utf-8

# class manage interaction with keyboard and pygame screen
import pygame



class GamePad():

    def __init__(self, game,lock_diagonal=False, player_move="cell"):
        self.mouse_position = (0, 0)
        self.__direction = (0, 0)
        self.key_states = {}
        self.close = False
        # lock diagonal move
        self.lock_diagonal = lock_diagonal
        self.game = game
        self.player_move = player_move


    def is_key(self, keyname):
        """
        return if a key is pressed
        :param keyname: string
        :return:
        """
        for event in self.key_states:
            if event.type == pygame.KEYDOWN:
                return event.key == keyname

    def is_move(self):
        """ return if movement """
        return not self.direction == (0, 0)

    # return direction move
    @property
    def direction(self):
        return self.__direction

    # direction setter
    @direction.setter
    def direction(self, dir):
        self.__direction = dir

    def hook_events(self):
        """ events keyboard"""
        
        self.key_states = self.game.event.get()
        dx, dy = (0, 0)
        """ save keypress event """
        for event in self.key_states:
            # check for closing window
            if event.type == pygame.QUIT:
                self.close = True
            if self.player_move == "cell":
                if event.type == pygame.KEYDOWN:
                    if self.lock_diagonal:
                        if event.key == pygame.K_LEFT:
                            dx = -1
                        elif event.key == pygame.K_RIGHT:
                            dx = 1
                        elif event.key == pygame.K_UP:
                            dy = -1
                        elif event.key == pygame.K_DOWN:
                            dy = 1

                    else:
                        if event.key == pygame.K_LEFT:
                            dx = -1
                        if event.key == pygame.K_RIGHT:
                            dx = 1
                        if event.key == pygame.K_UP:
                            dy = -1
                        if event.key == pygame.K_DOWN:
                            dy = 1

        if self.player_move == "smooth":
            keys = self.game.key.get_pressed()
            if keys[pygame.K_LEFT]:
                dx = -1
            elif keys[pygame.K_RIGHT]:
                dx = 1
            elif keys[pygame.K_UP]:
                dy = -1
            elif keys[pygame.K_DOWN]:
                dy = 1

        self.direction = (dx, dy)


