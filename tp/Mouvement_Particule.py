
import sys 
from vecteur3D import Vecteur3D
from math import *
import pygame
import matplotlib.pyplot as plt 
from pylab import show, legend, title
from pygame.locals import * 

from particule import * 


""" Test de trajectoire parabolique"""

Test = Particule(10)

Vo = Vecteur3D(10/sqrt(2), 10/sqrt(2) , 0) # 10 m/s avec un angle de pi/4
Theta = atan2(Vo.y , Vo.x)


t = (2*sin(Theta)*(Vo.Module()))/g # temps pour atteindre la portée 
d = (sin(2*Theta)*(Vo.Module())**2)/g # portée 
print("Temps ppour atteindre la portée : " , t,"s")
print("Distance de portée : " , d ,"m")


Time = [0]
for _ in np.linspace(0, t , 100): 
    
    Test.Simumation(_ ,  Vo ) 
    Time.append(_)


Test.plot("Positions") 
plt.grid() 
plt.show() 
