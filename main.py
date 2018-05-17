#! /usr/bin/env python3
# coding: utf-8

# dependence
from master.manager import GameManager


def main():
    """ main function load project"""
    # create game manger
    game = GameManager()

    # main loop execute game until closed
    while not game.close:
        game.run()

    # close pygame
    game.quit()
    # close script
    quit()


# if file execute by user start main function
if __name__ == '__main__':
    main()