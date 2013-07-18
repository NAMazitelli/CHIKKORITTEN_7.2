#! /usr/bin/env python
# Clase Personaje
# Copyright (C) 2012  EGGBREAKER <eggbreaker@live.com.ar>

ATK_SPEED_DPS = 12
MOV_SPEED_DPS = 8
DAMAGE_DPS = 8
HITPOINTS_DPS = 100
STATE_WALK = 'walk'
STATE_FEAR = 'fear'
STATE_STUN = 'stun'
STATE_RUN = 'run'
COST_RUN = 12
COST_WALK = 12
WALK_ESC = 1
RUN_ESC = 1.5


from AEstrella import AEstrella
from lectormapa import Mapa

class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

x = Infix(lambda a,b:tuple([x+y for x, y in zip(a, b)]))

y = Infix(lambda a,b:tuple([a*y for y in b]))

class Personaje:
    #AtkSpeed
    #MovSpeed
    #Sprite
    #Posicion
    ActionPoints = 100

    def __init__(self, AtkSpeed = 10, MovSpeed = 10, Posicion = (5,5)):
            self.AtkSpeed = AtkSpeed
            self.MovSpeed = MovSpeed
            self.Posicion = Posicion

class DPS(Personaje):
    AtkSpeed = ATK_SPEED_DPS
    MovSpeed = MOV_SPEED_DPS
    Damage   = DAMAGE_DPS
    HitPoints = HITPOINTS_DPS
    Estado    = STATE_WALK
    Habilidades = []

    def __init__(self, Posicion = (5,5)):
            self.Posicion = Posicion

    def autoattack(self, target):
            self.ActionPoints -= (30 - self.AtkSpeed)
            target.HitPoints -= self.Damage

            return self, target, (30 - self.AtkSpeed)

    def canMove(self, mapa, comando):
            #movimiento = AEstrella(mapa, self.Posicion, destino)
            if (self.Estado == STUN) or (self.Estado == FEAR):
                return False, NONE
            elif self.Estado == RUN:
                if mapa.pos(self.Posicion |x| (RUN_ESC |y| comando)) == LIBRE:
                    return True, COST_RUN
                else:
                    return False, NONE
            else:
                if mapa.pos(self.Posicion |x| (WALK_ESC |y| comando)) == LIBRE:
                    return True, COST_WALK
                else:
                    return False, NONE

    def move(self, comando):
            self.Posicion = self.Posicion |x| (RUN_ESC |y| comando)
            if self.Estado == STATE_RUN:
                self.ActionPoints -= COST_RUN
            else:
                self.ActionPoints -= COST_WALK

mapa = Mapa()

unDPS = DPS((2,3))
unDPS.move((0,1))

print unDPS.Posicion
print unDPS.ActionPoints
