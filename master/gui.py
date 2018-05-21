#! /usr/bin/env python3
# coding: utf-8
import pygame

from master.settings import GUI_LAYER, CYAN, GUI_SPRITESHEET, TILESIZE, RED
from master.spritesheet import Spritesheet


class GuiElement():
    """ manage gui element"""

    def __init__(self, x, y):
        self.__visible = False
        self.x = x
        self.y = y
        self.image = False
        self.rect = False
        self.text = False
        self.font = False
        self.font_size = 16
        self.font_color = (255, 255, 255)
        self.active = False
        self.active_image = False
        self.active_rect = False

    def draw(self, surface):
        """

        :param surface:
        :return:
        """
        if self.__visible:
            if self.active and self.active_image:
                surface.blit(self.active_image, self.active_rect)
            else:
                surface.blit(self.image, self.rect)
            if self.text:
                surface.blit(self.text.image, self.text.rect)

    def change_text(self, text):
        """

        :param text:
        :return:
        """

        self.text.image = self.text.font.render(text, 1, self.text.font_color)
        #self.text.rect = self.text.image.get_rect()

    def set_visible(self, visible):
        self.__visible = visible

    def set_active(self, visible):
        self.active = visible

    @property
    def is_visible(self):
        return self.__visible

    def set_image(self, image):
        self.image = image
        self.rect = self.image.get_rect()


class Gui():
    """ this manage gui """
    def __init__(self, manager):
        self.game = manager
        self.elements = {}
        self.spritesheet = Spritesheet(GUI_SPRITESHEET, TILESIZE, TILESIZE)
        self.new()

    def new(self):
        """ add gui interface """
        self.add_element("menu", self.create_menu())
        self.add_element("message", self.create_message())
        self.add_element("btn_start", self.create_btn("START",128,128))
        self.create_items()




    def make_image(self, x=0, y=0, row=0, col=0, rows=1, cols=1):
        """

        :param row: int
        :param col: int
        :param rows: int
        :param cols: int
        :return:
        """
        # create a surface to draw the element
        el = GuiElement(x, y)
        el.image = self.spritesheet.get_section_image(row, col, rows, cols)

        el.rect = el.image.get_rect()
        el.rect.x = x
        el.rect.y = y
        return el

    def make_text(self, x, y, text, color=(255,255,0), font_size=16):
        """

        :param x: int
        :param y: int
        :param text: string
        :return:
        """
        # create a surface to draw the element
        el = GuiElement(x, y)
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        el.font = pygame.font.SysFont("robot", font_size, bold=False)

        # render text
        el.image = el.font.render(text, 1, color)
        el.rect = el.image.get_rect()
        el.rect.x = x
        el.rect.y = y
        el.font_size = font_size
        el.font_color = color
        return el

    def make_panel(self, x, y, width, height, color=(0, 110, 250)):
        """

        :param x: int
        :param y: int
        :param width: int
        :param height: int
        :param color: tuple rgb
        :return:
        """
        # create a surface to draw the element
        panel = GuiElement(x, y)

        temp_surface = pygame.Surface((width, height))
        temp_surface.set_alpha(210)
        temp_surface.fill((255, 255, 255))
        rect = pygame.Rect(0, 0, width, height)
        pygame.draw.rect(temp_surface, (0, 0, 0), rect)
        rect.height = 5
        pygame.draw.rect(temp_surface, color, rect)
        rect.y = 5
        rect.height = height - 5
        pygame.draw.rect(temp_surface, color, rect, 1)

        panel.image = temp_surface
        panel.rect = temp_surface.get_rect()
        panel.rect.x = x
        panel.rect.y = y

        return panel

    def make_panel_text(self, x, y, width, height, text, color=(0, 110, 250), text_color=(255,255,255),font_size=16):
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param text:
        :param color:
        :return:
        """
        panel = self.make_panel(x, y, width, height, color)
        label = self.make_text(x+15, y+15, text,color=text_color, font_size=font_size)
        label.set_visible(True)
        panel.text = label
        return panel

    def create_menu(self):
        """ create menu bar """
        menu = self.make_image(0, 0, 0, 0, 1, 16)
        menu.set_visible(True)
        return menu

    def create_message(self):
        """ create message box """
        args = {
            'x' : 256,
            'y' : 64,
            'row' : 1,
            'col' : 8,
            'rows' : 2,
            'cols' : 8,
        }
        panel = self.make_image(**args)
        panel.set_visible(True)
        label = self.make_text(args['x'] + 32, args['y'] + 32, "",color=(255,255,0))
        label.set_visible(True)
        panel.text = label
        return panel

    def create_btn(self, label, x, y):
        """ create btn with event """
        args = {
            'x': x,
            'y': y,
            'row': 2,
            'col': 4,
            'rows': 1,
            'cols': 3,
        }

        btn_label = self.make_text(args['x'] + 32, args['y'] + 24, label , color=(25, 25, 25), font_size=24)
        btn_label.set_visible(True)
        btn_label.rect.centerx = args['x']+ 96
        active_btn = self.make_image(**args)
        active_btn.text = btn_label

        args = {
            'x': x,
            'y': y,
            'row': 2,
            'col': 1,
            'rows': 1,
            'cols': 3,
        }
        btn = self.make_image(**args)
        btn.text = btn_label
        btn.set_visible(True)
        btn.active_image = active_btn.image
        btn.active_rect = active_btn.rect

        return btn

    def create_items(self):
        args = {
            'x': 512,
            'y': 0,
            'row': 1,
            'col': 3,
            'rows': 1,
            'cols': 1,
        }
        ether = self.make_image(**args)
        ether.set_visible(True)
        args = {
            'x': 576,
            'y': 0,
            'row': 1,
            'col': 4,
            'rows': 1,
            'cols': 1,
        }
        aiguille = self.make_image(**args)
        aiguille.set_visible(True)
        args = {
            'x': 640,
            'y': 0,
            'row': 1,
            'col': 5,
            'rows': 1,
            'cols': 1,
        }
        tube = self.make_image(**args)
        tube.set_visible(True)
        self.add_element("ether", self.create_icon(ether.x, 0, ether))
        self.add_element("aiguille", self.create_icon(aiguille.x, 0, aiguille))
        self.add_element("tube", self.create_icon(tube.x, 0, tube))

    def create_icon(self, x, y, active_img):
        """

        :param x:
        :param y:
        :param active_img:
        :return:
        """
        args = {
            'x': x,
            'y': y,
            'row': 2,
            'col': 0,
            'rows': 1,
            'cols': 1,
        }
        item = self.make_image(**args)
        item.active_image = active_img.image
        item.active_rect = active_img.rect

        item.set_visible(True)
        return item

    def add_element(self, name, gui_element):
        """

        :param name: string
        :param gui_element: guielement
        :return:
        """
        self.elements[name] = gui_element

    def set_visible(self, name, visible):
        """
        change element visibility
        :param name: string
        :param visible: bool
        :return:
        """
        if self.elements[name]:
            self.elements[name].set_visible(visible)

    def active(self, name, visible):
        """
        active a element
        :param name: string
        :param visible: boll
        :return:
        """
        if self.elements[name]:
            self.elements[name].set_active(visible)

    def draw(self, surface):
        """

        :param surface:
        :return:
        """
        for name, element in self.elements.items():
            element.draw(surface)
            pygame.draw.rect(surface, RED, element.rect, 1)


