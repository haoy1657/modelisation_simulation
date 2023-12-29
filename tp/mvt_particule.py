import sys 
from particule import Particule
from vecteur3D import Vecteur3D
from math import *
import pygame
import matplotlib.pyplot as plt 
from pylab import show, legend, title
from pygame.locals import * 


""" Test de trajectoire parabolique"""

Test = Particule(10)
# On peut savoir que c'est 10 m/s, 45 degrés grâce aux composantes du vecteur Vo.

# Ici, on a :

# Vo.x = 10/sqrt(2), ce qui correspond à la composante en x de la vitesse initiale.
# Vo.y = 10/sqrt(2), ce qui correspond à la composante en y de la vitesse initiale.
# Vo.z = 0, car la particule ne se déplace pas selon l'axe z.
# On peut calculer la norme de Vo (qui correspond à la vitesse initiale) en utilisant la formule :

# ||Vo|| = sqrt(Vo.x^2 + Vo.y^2 + Vo.z^2)

# Ici, ||Vo|| = sqrt((10/sqrt(2))^2 + (10/sqrt(2))^2 + 0^2) = sqrt(200) = 10 m/s.

# On peut également calculer l'angle entre Vo et l'axe x en utilisant la fonction atan2 :

# Theta = atan2(Vo.y , Vo.x)

# Ici, Theta = atan2(10/sqrt(2) , 10/sqrt(2)) = 45°.

Vo = Vecteur3D(10/sqrt(2), 10/sqrt(2) , 0) 
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
