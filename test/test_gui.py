#! /usr/bin/env python3
# coding: utf-8
import sys, os


GamePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, GamePath)

from master.settings import  SCREEN_SIZE
from master.gui import Gui, GuiElement
import pygame as GAME
# pygame initialization
GAME.init()
# create a new window
SCREEN = GAME.display.set_mode(SCREEN_SIZE)
# initialise object manage game time
DT = GAME.time.Clock()


class TestGui(object):

    # test create gui
    def test_create_gui(self):
        gui = Gui(GAME)
        menu = gui.menu['menu']
        assert menu.is_visible == False
        menu.set_visible(True)
        assert menu.is_visible == True


    # test create image
    def test_create_image(self):
        gui = Gui(GAME)
        image = gui.make_image(0, 0, 0, 0, 2, 2)
        assert image.rect.width == 128
        assert image.rect.height == 128

        image = gui.make_image(0, 0, 2, 3, 5, 6)
        assert image.rect.width == 384
        assert image.rect.height == 320

    # test add element
    def test_add_element(self):
        gui = Gui(GAME)
        gui.add_element("btn", gui.make_image(0, 0, 0, 0, 2, 2))
        assert isinstance(gui.elements["btn"],  GuiElement)