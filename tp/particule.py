import sys
from vecteur3D import Vecteur3D
from math import *
import pygame
import matplotlib.pyplot as plt 
from pylab import show, legend, title
from pygame.locals import * 


class Particule(object):
    def __init__(self, position_i=Vecteur3D(),vitesse_i=Vecteur3D(),masse=1.0,color='blue',name='particule'):
        self.position=[position_i]
        self.vitesse=[vitesse_i]
        self.acceleration=[Vecteur3D()]
        self.forces=[Vecteur3D()]
        self.mass=masse
        self.color=color
        self.name=name
      
        
   
        
    def __str__(self):
        return f"Particule({self.name}, {self.position[-1]})"
    
    
    def __repr__(self):
        return str(self)
        
    
    def getPos(self):
        return self.position[-1]
    
    def getVit(self):
        return self.vitesse[-1]
    
    def getForce(self):
        return self.forces[-1]

    def setForces(self,Force=Vecteur3D()):
        self.forcesExt.append(Force)
    
    
    def PFD (self):
        a=Vecteur3D()
        a=self.getForce()*(1/self.mass)
        self.acceleration.append(a)
    

    
    def sim(self, step):
        v = Vecteur3D()
        new_v = v + self.acceleration[-1] * step
        self.vitesse.append(new_v)

        p = self.getPos()
        new_p = p + v * step + 0.5 *self.acceleration[-1] * step ** 2
        self.position.append(new_p)

    
    


    def plot(self, Mode=None, Time=None):
        pos_arr = np.array([p.get_array() for p in self.position])
        X, Y = pos_arr[:,0], pos_arr[:,1]
        plt.plot(X, Y, color=self.color, label=self.name)
        plt.show()
        
        
    def draw(self,screen, scale=1):
        size= 5
        
        #Position
        X = int(scale*self.getPos().x)
        Y = int(scale*self.getPos().y) 
        
        pygame.draw.circle(screen,self.color,(X,Y),size*2,size)
        
        # Vecteur vitesse
        vit = self.getVit()
        VX = int(scale*vit.x) + X
        VY = - int(scale*vit.y) + Y  # pour inverser l'axe Y de l'affichage
        
        
        pygame.draw.line(screen,self.color,(X,Y),(VX,VY))

        

class ForceCst:
    def __init__(self,fc= Vecteur3D(),*args):
        self.fc=fc
        self.agents=list(args)
        
    
    def __str__(self):
        return f"Force constante({self.fc})"
    
    def effect(self, p):
        return self.fc if not self.agents or p in self.agents else Vecteur3D()


class Gravite:
    def __init__(self,direction=Vecteur3D()):
        self.direction=direction
        
    def effect(self,p):
        return p.mass * self.direction
    
    
class Viscosite:
    def __init__(self,coeff):
        self.coeff=coeff
    
    def effect(self,p):
        return p.getVit()*self.coeff
    
    
    
class Ressort(object):
    def __init__(self,p0,p1,raideur=0.,amortissement=.0,l0=0):
        self.raideur = raideur
        self.l0 = l0
        self.p0 = p0
        self.p1 = p1
        self.amortissement=amortissement
        # La liaison pivot relie deux "particules" p0 et p1
        
    def effect(self,p):
        if p is self.p2:
            n=self.p2.getPosition() - self.p1.getPosition() 
            v= (self.p2.getSpeed() - p.getSpeed()) ** n
        
        elif p is self.p1:
            n=self.p1.getPosition() - self.p2.getPosition() 
            v= (self.p1.getSpeed() - p.getSpeed()) ** n
        
        else: return Vecteur3D()
        
        force = ((n.mod()-self.l0) * self.raideur + self.amortissement * v) * n.norm()
        
        return force
    
class Univers() :
    
    def __init__(self,name="plage",t0=0, step=0.1,*args):
        self.name = name
        self.temps=[t0]
        self.population=[]
        self.step=step
        self.sources=[]
    
    def addSource(self,*args):
        sources = list(args)
        self.sources += sources
    
        
    def addAgent(self,*args):
        agents = list(args)
        self.population+=agents
        
    def simule(self):
        for a in self.population:
            Ftot=Vecteur3D()
            for f in self.sources:
                Ftot += f.effect(a)
            
            a.setForces(Ftot)
            a.PFD()
            a.sim(self.step)
            
        self.temps.append(self.temps[-1]+self.step)
    
    def plot(self):
        for i in self.population:
            i.plot()
        
    def gameInit(self,W,H,fps=60,background=(0,0,0),scale=1):
        
        
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen= pygame.display.set_mode((W,H))
        self.background=background
        self.fps=fps
        self.scale=scale
        self.run=True
        
        pygame.display.set_caption(self.name)
        self.gameKeys = pygame.key.get_pressed()

        
    def gameUpdate(self):
        
        now=self.temps[-1]
        while now< (now+(1/self.fps)):
            self.simule()
        
        font_obj=pygame.font.Font('freesansbold.ttf',24)
        text_surface_obj = font_obj.render(str(now)[:6], True, self.background)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (25, 10)

        self.screen.fill(self.background)
        
        for p in self.population:
            p.gameDraw(self.screen,self.scale)
        
        
        self.screen.blit(text_surface_obj,(5,10))
        pygame.display.update()

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.run= False 
        
        self.gameKeys = pygame.key.get_pressed()   
        self.clock.tick()
    
if __name__ == "__main__": 
    

    # Création des particules
    boule = Particule(name='boule', masse=1, position_i=Vecteur3D(0.2, 0, 0), vitesse_i=Vecteur3D(1, 0, 0))
    pivot = Particule(name='pivot', position_i=Vecteur3D(0.5, 0.5), color='black')
    
    # Création du simulateur avec pas de temps de 1ms (nécessaire pour bien simuler le ressort)
    Monde = Univers(step=0.01)
    
    # Ajout des agents (particules et point fixe)
    Monde.addAgent(boule)
    Monde.addAgent(pivot)
    
    # Création du ressort entre la particule et le point fixe
    l0 = (pivot.getPos() - boule.getPos()).mod()
    ressort = Ressort(pivot, boule, raideur=1000, amortissement=100, l0=l0)

    
    # Ajout des forces au simulateur
    Monde.addSource(Gravite(Vecteur3D(0, -9.81, 0)))
    Monde.addSource(Viscosite(0.01))
    Monde.addSource(Ressort)
    
    # Initialisation de l'affichage
    Monde.gameInit(800, 600, background='white', scale=200)
    
    # Boucle de simulation
    while Monde.run:
        # Mise à jour des forces
        
        
        # Interactivité
        if Monde.gameKeys[K_ESCAPE] or Monde.gameKeys[K_q]:
            Monde.run = False
        
        # Mise à jour de la simulation
        Monde.gameUpdate()
        
    # Affichage des résultats
    Monde.plot()
    plt.title(Monde.name)
    plt.legend()
    plt.show()




