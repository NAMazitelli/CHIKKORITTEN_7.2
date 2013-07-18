#! /usr/bin/env python
# Clase Input
# Copyright (C) 2012  EGGBREAKER <eggbreaker@live.com.ar>

import pygame
from pygame.locals import *

RIGHT, UP, LEFT, DOWN = (1,1), (1,-1), (-1,-1), (-1,1)
NE, SE, NO, SO = (0,-1), (1,0), (-1,0), (0,1)
dKEY2DIR = {275: RIGHT, 273:DOWN, 276:LEFT, 274:UP}

class Input():
    def __init__(self):
        self.Commands = []
        self.Order = (0,0)
        self.Quit = False

    def update(self):
        for anEvent in pygame.event.get():
            if anEvent.type == pygame.KEYDOWN:
                if anEvent.key in [dKEY2DIR.keys]:
                    self.append(Key2Dir[anEvent.key])
                if anEvent.key == K_ESCAPE:
                    self.Quit = True
            if anEvent.type == pygame.KEYUP:
                if anEvent.key in [dKEY2DIR.keys]:
                    self.remove(Key2Dir[anEvent.key])

    def updateOrder(self):
        for Command in self.Commands:
            xAcum += Command[0]
            yAcum += Command[1]

        if abs(xAcum) >= 1:
            xAcum = 1
        else:
            xAcum = -1

        if abs(yAcum) >= 1:
            yAcum = 1
        else:
            yAcum = -1

        self.Order = xAcum, yAcum

    def append(self, aCommand):
        self.Commands.append(aCommand)
        self.updateOrder()

    def remove(self, aCommand):
        assert not self.Commands.empty()
        self.Commands.remove(aCommand)
        self.updateOrder()

    def empty(self):
        return len(self.Commands) == 0

