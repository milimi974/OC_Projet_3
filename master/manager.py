#! /usr/bin/env python3
# coding: utf-8
import math
import pygame
from os import path
from pygame.math import Vector2

from master.camera import Camera
from master.gamepad import GamePad
from master.gui import Gui
from module.map import Map, Obstacle, Item
from master.settings import *
from module.charcater import Player, Mob


class GameManager():
    """ this class manage game """

    # close game
    close = False

    def __init__(self):
        """ constructor """
        # pygame initialization
        self.game = pygame
        self.game.init()
        self.pause = False
        self.start = False
        self.items_found = []
        self.level_end = False

        # create a new window
        self.screen = self.game.display.set_mode(SCREEN_SIZE)
        self.game.display.set_caption(GAME_SCREEN_NAME)
        # initialise object manage game time
        self.clock = self.game.time.Clock()
        if PLAYER_MOVE == "cell":
            self.game.key.set_repeat(200, 100)
        self.gui = Gui(self)
        self.gui.set_mainmenu_visible(True)

        # sound loading
        pygame.mixer.music.load(path.join(MUSICS, BG_MUSIC))
        pygame.mixer.music.set_volume(0.2)
        self.effects_sounds = {}
        for type in EFFECTS_SOUNDS:
            self.effects_sounds[type] = pygame.mixer.Sound(path.join(SOUNDS, EFFECTS_SOUNDS[type]))

        self.zombie_roar = []
        for snd in MOB_MOAN_SOUNDS:
            self.zombie_roar.append(pygame.mixer.Sound(path.join(SOUNDS, snd)))

        self.new()
        pygame.mixer.music.play(-1)

    def new(self, level=0):
        """
        initialize new instance for game
        :return:
        """

        self.level_end = False
        # gamepad
        self.gamepad = GamePad(self.game,
                               lock_diagonal=PLAYER_DIAGONAL_MOVE,
                               player_move=PLAYER_MOVE)
        # create a new sprite group
        self.all_sprites = self.game.sprite.LayeredUpdates()
        self.walls = self.game.sprite.Group()
        self.items = self.game.sprite.Group()
        self.mobs = self.game.sprite.Group()

        # init map
        self.map = Map(self, level)

        # camera
        self.camera = Camera(self.map.width, self.map.height)

        # init gui
        args = {
            'width': WIDTH,
            'height': 64,
            'x': 0,
            'y': 0,
        }

        # self.player = Player(self, 0, 0)
        layer = self.map.get_items_layer()
        tmxdata = self.map.tmxdata
        # collide object
        for tile_object  in tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, self.object_tmx_center(tile_object))

            if tile_object.name == 'mob':
                Mob(self, self.object_tmx_center(tile_object), tile_object.type, tile_object.name)

            if tile_object.name == 'item':
                object_pos = self.object_tmx_position(tile_object, tmxdata.tilewidth, tmxdata.tileheight)
                if tile_object.type == 'goal':
                    image = pygame.Surface((64,64), pygame.SRCALPHA)
                    Item(self, self.object_tmx_center(tile_object), image, tile_object.name, tile_object.type)
                else:
                    for x, y, image in layer.tiles():
                        tile_pos = (x*tmxdata.tilewidth, y*tmxdata.tileheight)
                        if object_pos == tile_pos:
                            Item(self, self.object_tmx_center(tile_object), image, tile_object.name, tile_object.type)

            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def run(self):
        """ run game """
        # update clock game time by frame rate
        dt = self.clock.tick(FPS) / 1000
        self.events()

        if not self.start:
            # game not start
            self.gui.update(self, dt)
            # draw gui
            self.gui.draw(self.screen)

            # self.all_sprites.draw(self.screen)
            # drawing everything, flip the display
            self.game.display.flip()
        else:
            if self.pause:
                #game pause
                pass
            else:
                # game running
                self.draw()
                self.update(dt)

    def update(self, dt):
        """ update module
        Keyword arguments:
        dt -- integer Delta time time between 2 update Main Loop

        """

        self.all_sprites.update(dt)
        self.camera.update(self.player)
        # player hit items
        hits = self.game.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == "item":
                if hit.name == "goal" and self.level_end:
                    self.next_map()
                    self.level_end = False
                elif hit.name == "health":
                    self.player.health += int(PLAYER_HEALTH*0.25)
                    self.effects_sounds['health_up'].play()
                    if self.player.health > PLAYER_HEALTH:
                        self.player.health = PLAYER_HEALTH
                    hit.kill()
                elif not hit.name == "goal":
                    self.effects_sounds['item_pickup'].play()
                    self.add_item(hit)
                    hit.kill()
        # player hit mobs
        hits = self.game.sprite.spritecollide(self.player, self.mobs, False)
        for hit in hits:
            if hit.type == "boss":
                if len(self.items_found) == 3 :
                    hit.kill()
                    self.level_end = True
                else:
                    self.new(self.map.current_map)
                self.items_found = []
            else:
                self.player.health -= MOB_DAMAGE
                self.effects_sounds['hit'].play()
                if self.player.health <= 0:
                    self.effects_sounds['death'].play()
                    self.new(self.map.current_map)
                    self.items_found = []
                    self.player.health = PLAYER_HEALTH

        self.gui.menu["hp"].bar_value = self.player.health
        self.gui.update(self, dt)

    def next_map(self):
        """ move to next map """
        next_level = self.map.next()
        if next_level:
            self.new(next_level)
            self.gui.menu['level'].change_text("CARTE {}".format(str(next_level+1)))
            self.effects_sounds['level_start'].play()
        else:
            self.quit()

    def add_item(self, item):
        """
        player found item
        :param item: Item
        :return:
        """
        self.items_found.append(item.name)

    def object_tmx_center(self, object):
        """
        return position of object tmx center
        :param object: tmx
        :return:
        """
        x = object.x + (object.width / 2)
        y = object.y + (object.height / 2)
        return Vector2(x, y)

    def object_tmx_position(self, object, tilewidth, tileheight):
        """
        return position of object tmx x y
        :param object: tmx
        :return:
        """
        x = math.floor(object.x / tilewidth ) * tilewidth
        y = math.floor(object.y / tilewidth ) * tileheight
        return (x, y)

    def draw(self):
        """ draw module """
        # clear window
        self.screen.fill(BLACK)

        # draw map
        self.screen.blit(self.map.map_img, self.camera.apply_rect(self.map.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if DEBUG:
               pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.rect), 1)

        if DEBUG:
            for sprite in self.walls:
               pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.rect), 1)



        # draw gui
        self.gui.draw(self.screen)

        # self.all_sprites.draw(self.screen)
        if DEBUG:
            self.game.display.set_caption(str(self.player.health))
            self.draw_grid()
        # drawing everything, flip the display
        self.game.display.flip()

    def draw_grid(self):
        """ draw a grid """
        for x in range(0, WIDTH, TILESIZE):
            self.game.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, TILESIZE):
            self.game.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def events(self):
        """
        manage game events
        :return:
        """
        # process input (events)
        self.gamepad.hook_events()
        # click on screen actions
        if self.gamepad.leftclick and self.gui.btn["btn_start"].hover and not self.start:
            self.start = True
            self.gui.set_mainmenu_visible(False)
            self.effects_sounds['level_start'].play()

        # if user close the game
        if self.gamepad.close :
            self.close = True

    def quit(self):
        """ leaved the game """
        self.game.quit()
