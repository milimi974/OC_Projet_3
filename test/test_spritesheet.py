#! /usr/bin/env python3
# coding: utf-8
import sys, os

import pygame

GamePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, GamePath)
ASSET_FOLDER = os.path.join(GamePath, "assets")

from master.spritesheet import Spritesheet, Animation


class TestSpritesheet(object):

    # test attributes is settings
    def test_attributes_settings(self):

        sprite = Spritesheet(os.path.join(ASSET_FOLDER,"spritesheet/character.png"), 41, 44)
        assert sprite.rows == 4
        assert sprite.cols == 2
        assert sprite.totalCellCount == 8
        assert len(sprite.cells) == 4

    # test mapping sprite sheet
    def test_mapping_spritesheet(self):
        sprite = Spritesheet(os.path.join(ASSET_FOLDER, "spritesheet/character.png"), 41, 44)
        cell = sprite.cells[0][0]
        assert isinstance(cell,  pygame.Surface)
        cell = sprite.cells[0][1]
        assert isinstance(cell,  pygame.Surface)

    # test if an image created
    def test_image_created(self):
        sprite = Spritesheet(os.path.join(ASSET_FOLDER, "spritesheet/character.png"), 41, 44)
        image = sprite.get_image(0,0)
        assert type(image) == pygame.Surface

    # test animation object
    def test_animation_object(self):
        sprite = Spritesheet(os.path.join(ASSET_FOLDER, "spritesheet/character.png"), 41, 44)
        animation = sprite.get_animation(0, 0, 2)
        assert isinstance(animation,  Animation)
        assert type(animation.image) == pygame.Surface

    # test create section_image
    def test_create_section_image(self):
        sprite = Spritesheet(os.path.join(ASSET_FOLDER, "spritesheet/gui.png"), 64, 64)
        image = sprite.get_section_image(0, 0, 1, 16)
        # if a surface
        assert isinstance(image,  pygame.Surface)
        # if size right
        rect = image.get_rect()
        assert rect.width == 1024
        assert rect.height == 64
