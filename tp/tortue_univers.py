# -*- coding: utf-8 -*-

from vecteur3D import *
from numpy import pi, arange, sin, cos
from tortue import *
from pylab import legend, show, grid

plage = Univers()



toto=Tortue()
toto.speedRot=pi/5
toto.speedTrans= .6
mario = Tortue(Vecteur3D(-10,-10),pi/2,name='mario',color='blue')
luigi=Tortue(Vecteur3D(-5,7),pi/6,name='luigi',color='green')
#mario.speedRot = pi/4
mario.speedTrans = .51
luigi.speedTrans=0.71

plage.add(toto)
plage.add(mario)
plage.add(luigi)

while plage.temps[-1] <100:
    mario.controlGoTo(toto.position[-1])
    luigi.controlGoTo(mario.position[-1])
    plage.simule()
    
plage.plot()
legend()
grid()
show()


