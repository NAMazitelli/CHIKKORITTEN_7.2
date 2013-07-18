#! /usr/bin/env python
# Clase Turno, Action, Movimiento, AutoAtaque
# Copyright (C) 2012  EGGBREAKER <eggbreaker@live.com.ar>

from char import Personaje
from lectormapa import Mapa

T_MOVEMENT = 'mov'
T_WAIT = 'wait'
T_AA = 'aa'
T_SKILL = 'skill'

class Turno():
    ActionLists = []

class Action():
    Char = None
    Type = None
    Forced = False

    def __init__(self, Char, Type, Forced = False):
        self.Char = Char
        self.Type = Type
        self.Forced = Forced

class Movimiento(Action):
    Type = T_MOVEMENT
    MovList = []

    def __init__(self, Char, Forced = False):
        self.Char = Char
        self.Forced = Forced
        self.MovList.append(Char.Posicion)

    def addMove(self, Pos):
        self.Movlist.append(Pos)

class AutoAtaque(Action):
    Type = T_AA

    def __init__(self, Char, Target, Forced = False):
        self.Char = Char
        self.Target = Target
        self.Forced = Forced





