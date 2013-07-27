#! /usr/bin/env python
# Clase Turno, Action, Movimiento, AutoAtaque
# Copyright (C) 2012  EGGBREAKER <eggbreaker@live.com.ar>

from eb_lectormapa import Mapa


class Turno():
    ActionList = []
    
    def __init__(self):
        self.ActionList = []
    
    def getLastAction(self):
        if len(self.ActionList) == 0:
            return None
        return self.ActionList[-1].__class__.__name__
    
    def addAction(self, Action):
        self.ActionList.append(Action)

class Action():
    #Target = None
    Forced = False

    def __init__(self, Forced = False):
        self.Forced = Forced

class Movimiento(Action):
    MovList = []

    def __init__(self, Pos, Forced = False):
        self.Forced = Forced
        self.MovList.append(Pos)
        
    def addPos(self, Pos):
        self.MovList.append(Pos)
        
    def isFirstMove(self):
        return len(self.MovList) == 0

class AutoAtaque(Action):

    def __init__(self, Char, Target, Forced = False):
        self.Target = Target
        self.Forced = Forced





