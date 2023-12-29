# -*- coding: utf-8 -*-

from vecteur3D import *
from numpy import pi, arange, sin, cos
from pylab import plot, show, legend
from tortue import *

tfin=10
step=0.6
temps= arange(0,tfin,step)

toto=Tortue() # création d'une instance de la classe Tortue qui utilise les valeurs par défaut de Tortue
toto.speedRot=pi/5
toto.speedTrans=0.6

mario=Tortue(Vecteur3D(4,0),name='Mario',color='blue') #création d'une instance de la classe Tortue qui spécifie une position initiale pour la tortue
mario.speedRot=pi/4
mario.speedTrans= 0.2

for i in temps:
    toto.speedRot=sin(i)
    mario.speedRot=cos(i)
    toto.move(step)
    mario.speedTrans= abs(0.9*sin(i)) # la valeur absolue est utilisée pour s'assurer que la vitesse de déplacement est toujours positive
    mario.move(step)
    
toto.plot()
mario.plot()
legend()
show()
