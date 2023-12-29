# -*- coding: utf-8 -*-

from vecteur3D import *
from numpy import pi
from tortue import *

rot= [0,pi/4,-pi/4,pi/3]
trans=[1,2,0.5,1]

toto=Tortue()

nbr=len(rot)
for i in range(nbr):
    toto.turn(rot[i])
    toto.walk(trans[i])
    

toto.plot()
show()
