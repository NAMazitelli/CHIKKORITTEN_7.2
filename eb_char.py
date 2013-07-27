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
FASE_P = 'planeamiento'
FASE_A = 'accion'

#           R,    G,    B
BLACK =     (0  , 0  ,  0  )
WHITE =     (255, 255,  255)
GREEN =     (0  , 160,  50 )
RED   =     (160, 25 ,  25 )

from eb_render import Render
from eb_turno import Turno, Action, Movimiento, AutoAtaque
from eb_lectormapa import Mapa

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


    def __init__(self, AtkSpeed = 10, MovSpeed = 10, Posicion = (5,5)):
            self.AtkSpeed = AtkSpeed
            self.MovSpeed = MovSpeed
            self.Posicion = Posicion
            
    def getAction(self):
        assert self.Turno.ActionList
        Action = self.Turno.ActionList[0]
        self.Turno.ActionList.remove(Action)
        
        return Action
    
    def Play(self, Action):
        if Action.__class__.__name__ == 'Movimiento':
            self.Posicion = Action.MovList[0][0]
            Action.MovList.remove(Action.MovList[0])
    
    def cambiaFase(self):
        if self.Fase == FASE_P:
            self.Fase = FASE_A
            self.PlaceHolderColor = RED
        else:
            self.Fase = FASE_P
            self.ActionPoints = 100
            self.PlaceHolderColor = GREEN

    def draw(self, render):
        render.drawPlaceHolder(self.PlaceHolderColor, self.Posicion[0], self.Posicion[1])

class DPS(Personaje):
    AtkSpeed = ATK_SPEED_DPS
    MovSpeed = MOV_SPEED_DPS
    Damage   = DAMAGE_DPS
    HitPoints = HITPOINTS_DPS
    Estado    = STATE_WALK
    PlaceHolderColor = GREEN
    Habilidades = []
    
    Fase = FASE_P
    ActionPoints = 100

    def __init__(self, Posicion = (5,5)):
            self.Posicion = Posicion
            self.Turno = Turno()

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
        if comando != (0,0):           
            #lastAction = self.Turno.getLastAction() 
            #if (lastAction == None) or lastAction != "Movimiento":
            #  self.Turno.addAction(Movimiento((self.Posicion, self.Estado)))
                
            if self.Estado == STATE_RUN:
                self.Posicion = self.Posicion |x| (RUN_ESC |y| comando)
                self.ActionPoints -= COST_RUN
            else:
                self.Posicion = self.Posicion |x| (WALK_ESC |y| comando)
                self.ActionPoints -= COST_WALK
            
            self.Turno.addAction(Movimiento((self.Posicion, self.Estado)))
            
            if self.ActionPoints < 0:
                self.cambiaFase()
                self.Posicion = self.Turno.ActionList[0].MovList[0][0]
            
            
            #self.Turno.ActionList[-1].addPos((self.Posicion, self.Estado))

