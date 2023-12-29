import sys
import pygame
from pygame.locals import *
from vecteur3D import *
from numpy import pi, arange, sin, cos
from tortue import *
from pylab import legend, show


plage = Univers(step=0.01)

toto=Tortue(R0=pi/3)
toto.speedRot=0 #pi/4
toto.speedTrans= 20
mario = Tortue(Vecteur3D(100,100),pi/4,name='mario',color='blue')
#mario.speedRot = pi/4
mario.speedTrans = 10

plage.add(toto)
plage.add(mario)

plage.gameInit(1024,768,background='gray',scale=1)

while plage.run:

    if plage.gameKeys[K_UP]:
        toto.speedTrans = toto.speedTrans+5
    if plage.gameKeys[K_DOWN]:
        toto.speedTrans = toto.speedTrans-5
    if plage.gameKeys[K_LEFT]:
        toto.speedRot = toto.speedRot-(pi/20)
    if plage.gameKeys[K_RIGHT]:
        toto.speedRot = toto.speedRot+(pi/20)
    if plage.gameKeys[K_ESCAPE]:
        plage.run = False

    mario.controlGoTo(toto.position[-1])
    
    plage.gameUpdate()
    
pygame.quit()
plage.plot()
legend()
show()


sys.exit()
