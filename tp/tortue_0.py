# -*- coding: utf-8 -*-

from vecteur3D import Vecteur3D
from numpy import pi
import matplotlib.pyplot as plt

rot = [pi/4, pi/5]
trans= [1,2,]

v0 = Vecteur3D() # Creation d'un vecteur 3D avec le constructeur par défaut 

traj = [v0] #Liste de vecteurs contenant les positions x et orientations z au cours du mouvement 
nbr_de_pas = len(trans)

for i in range (nbr_de_pas):
    vect = Vecteur3D(trans[i],0,rot[i]) # Mouvement = translation à 1D selon x et rotation selon z 
    theta = rot[i]+traj[-1].z # on somme les angles au cours du mouvement 
    # traj[-1] represente le dernier vecteur et traj[-1].z la derniere valeure angulaire de rotation faite par la tortue 
    
    # A l'itteration 0 , traj[-1] vaut le vecteur nul 
    
    vect.rotZ(theta) # recalcul de x,y avec une rotation de theta selon z 
    # Au depart , on crée un vecteur selon l'axe x (Vecteur3D(trans[i],0,rot[i])) et on vient le faire tourner selon z avec
    # la méthode rotZ 
    traj.append(vect+traj[-1]) # Addition des vecteurs precedents pour la position finale à l'itteration i (Chales)


print(traj)    



X=[]
Y=[]
for p in traj:
    X.append(p.x)
    Y.append(p.y)
    
plt.plot(X,Y)
plt.show()
