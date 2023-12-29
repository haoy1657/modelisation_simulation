# -*- coding: utf-8 -*-
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from vecteur3D import Vecteur3D as V3D

class Torseur:
    
    def __init__(self,P=V3D(),R=V3D(),M=V3D()):
        self.P=P
        self.R=R
        self.M=M
        
    def __str__(self):
        res= "La résultante: ({})".format(str(self.R))
        res+= " et Le moment : ({})".format(str(self.M))
        return res
    
    
    def __repr__(self) : 
        return str(self)

    def __neg__ (self) : 
        return (Torseur ( self.P , -self.R , self.P))

    def __sub__ (self , other) : 
        return (self + (-other))
    
    
    
    def changerPoint(self , point = V3D()) : 
    
        MD = self.M  + ( self.P  + (-point)) * self.R 
        self.P = point # Nouveau point 
        self.M = MD # Nouveau moment calculé 
        print(MD)
    
    
    def add ( self , Other) : 

        Other.changerPoint(self.P) #Changement de point pour assurer l'addition 
        
        Res = self.R + Other.R

        Moment = self.M + Other.M

        Point = self.P
        
        return Torseur(Res,Moment,Point)
        
        #Addition des torseurs ==> Au meme point


    def __eq__ ( self , Other) : 
       if self.P == Other.P:
            return bool((self.M == Other.M) &  (self.R == Other.R))
       else:
             return False


if __name__ == "__main__":  

    P = V3D() 
    R = V3D(1,0,0) 
    M = V3D(0,1,0)

    T = Torseur(R,M,P)
    pt = V3D( 2,1,0)
    T.changerPoint(pt)
    print(T, "\n")

    T2 = Torseur(V3D() , V3D(0,2,4) , V3D(1,0,8))
    print(T2==T)

    
    
