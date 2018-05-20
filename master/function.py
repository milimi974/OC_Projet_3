#! /usr/bin/env python3
# coding: utf-8

# function callback collision on custom box collision
def collide_hit_rect(entity1, entity2):
    return entity1.hit_rect.collliderect(entity2.rect)