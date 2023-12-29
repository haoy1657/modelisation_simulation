# -*- coding: utf-8 -*-
from vecteur3D import Vecteur3D
from math import pi,atan2
import pygame
from pygame.locals import *




def toPi(rad):
    """ calculate equivalent angle in  [-pi,pi] """ 
    # normalisation des angles en radians dans la plage [-pi,pi]
        
    angle = rad % (2*pi) 
    
    if angle > pi:
        angle = angle - (2*pi)
    
    elif angle < -pi:
        angle = 2*pi + angle
        
    return angle


class Tortue(object):

    
    def __init__(self,P0=Vecteur3D(),R0=0,speedTrans=0,speedRot=0,name='toto',color='red'):
        # initialisation des attributs de la tortue avec des valeurs par défaut ou les valeurs spécifiées par l'utilisateur 
        self.position=[P0]
        self.orientation=[R0]
        self.name=name
        self.color=color
        self.speedTrans = speedTrans
        self.speedRot = speedRot
        
    def __str__(self):
        # renvoie une chaine de caractères qui contient la dernière position de la tortue,son orientation, son nom et sa couleur
        return "Tortue ("+str(self.position[-1])+', '+str(self.orientation[-1])+', "'+self.name+'", "'+self.color+'")'
    
    def __repr__(self):
        # renvoie la chaine de caractères renvoyée par la méthode __str__(self)
        return str(self)
    
    def turn(self,angle):
        # fait tourner la tortue d'un angle donné en radians 
        # ajout de l'argument à l'orientation précédente de la tortue
        # nouvelle orientation stockée dans la liste self.orientation
        self.orientation.append(toPi(self.orientation[-1]+angle))
        
        
        
    def walk(self,dist):
        # fait avancer la tortue d'une distance donnée
        # la méthode crée un vecteur d représentant le déplacement de la tortue en utilisant la distance dist et l'orientation courante 
        # de la tortue, qui est stockée dans la liste self.orientation. Le vecteur de déplacement d est calculé en créant un nouveau vecteur 3D 
        # à partir de la distance dist, puis en le faisant tourner autour de l'axe Z par l'orientation courante de la tortue.
        d = Vecteur3D(dist).rotZ(self.orientation[-1])
        self.position.append(self.position[-1]+d)
    
    def move(self,step):
        #La méthode move(self, step) est une méthode de la classe Tortue qui fait avancer la tortue d'une distance correspondant à sa vitesse de déplacement (speedTrans) et faire tourner la tortue d'un angle correspondant à sa vitesse de rotation (speedRot). L'argument step représente le pas de temps de la simulation, et permet de calculer le déplacement et la rotation de la tortue pour ce pas de temps.
        rot = self.speedRot * step
        dist = self.speedTrans * step
        self.turn(rot)
        self.walk(dist)
    
    
    def controlGoTo(self,cible):
        #La méthode controlGoTo(self, cible) est une méthode de la classe Tortue qui permet de déplacer la tortue vers une cible donnée. L'argument cible est un vecteur 3D représentant la position de la cible.
        #En particulier, la méthode calcule le vecteur de déplacement dep nécessaire pour atteindre la cible en soustrayant la position courante de la tortue de la position de la cible. Elle calcule également l'angle de rotation angle nécessaire pour faire face à la cible en utilisant la fonction atan2() pour calculer l'angle entre l'axe x et le vecteur de déplacement.
        #La méthode calcule ensuite l'erreur d'angle errorA entre l'orientation courante de la tortue et l'angle de rotation nécessaire pour faire face à la cible. Elle utilise la fonction toPi() pour normaliser l'erreur d'angle dans la plage [-π, π], afin de garantir que l'orientation reste dans cette plage et d'éviter les valeurs d'angle ambiguës.
        
        dep = cible - self.position[-1]
        angle = atan2(dep.y,dep.x)
        errorA = toPi(angle - self.orientation[-1])
        
        self.speedRot =  .75 * errorA
        
        self.speedTrans = .65 * dep.mod()
        

    def plot(self):
        #a méthode plot(self) est une méthode de la classe Tortue qui permet de tracer le parcours de la tortue dans le plan x-y. Elle utilise la fonction plot() de la bibliothèque pylab pour tracer la trajectoire de la tortue en utilisant les coordonnées x et y de chaque position enregistrée dans la liste self.position
        #En particulier, la méthode crée deux listes vides X et Y pour stocker les coordonnées x et y de chaque position de la tortue. Elle parcourt ensuite la liste self.position en utilisant une boucle for pour extraire les coordonnées x et y de chaque position et les ajouter aux listes X et Y, respectivement.
        #Enfin, la méthode utilise la fonction plot(X, Y) pour tracer la trajectoire de la tortue en utilisant les listes X et Y créées précédemment.
        from pylab import plot
        X=[]
        Y=[]
        for p in self.position:
            X.append(p.x)
            Y.append(p.y)
    
        return plot(X,Y,color=self.color,label=self.name)
    
    def save(self):
        from pickle import dump
        file = open(self.name+'.dat','wb')
        dump(self,file)
        file.close

    def load(self,name=''):
        
        from pickle import load
        
        if name=='':
            name=self.name
        file = open(name+'.dat','rb')
        temp=load(file)
        self.position = temp.position
        self.orientation = temp.orientation
        #self.name = temp.name
        self.color = temp.color
        file.close
    
    def gameDraw(self,screen,scale):
        X=int(scale*self.position[-1].x)
        Y=int(scale*self.position[-1].y)
        
        vit=Vecteur3D(self.speedTrans).rotZ(self.orientation[-1])
        VX= int(scale*vit.x)+X
        VY=int(scale*vit.x)+Y
        
        size=int(scale*5)
        pygame.draw.circle(screen,self.color,(X,Y),size*2,size)
        pygame.draw.line(screen,self.color,(X,Y),(VX,VY))

        
        

    
                
class Univers(object):
    # initialisation de la classe qui prend en entrée le nom de l'univers, le temps initial t0, le pas de temps step, et une liste optionnelle d'agents à ajouter à l'univers 
    def __init__(self,name='la plage',t0=0, step=0.1,*args):
        self.name=name
        self.temps=[t0]
        self.population=[]
        self.step=step
    
    def add(self, agent):
        #ajouter un agent à l'univers
        self.population.append(agent)
    
    def simule(self):
        #La méthode simule(self) permet de simuler l'évolution de l'univers pour un pas de temps donné en appelant la méthode move() de chaque agent de la liste self.population. Cette méthode met à jour la position de chaque agent dans l'univers en fonction de sa vitesse de déplacement et de sa vitesse de rotation. Elle met également à jour le temps de simulation en ajoutant le pas de temps step à la liste self.temps
        for i in self.population:
            i.move(self.step)
        self.temps.append(self.temps[-1]+self.step)
    
    def plot(self):
        #tracer la position de chaque agent dans l'univers en appelant la méthode plot() de chaque agent de la liste self.population. Cette méthode peut être utilisée pour visualiser l'évolution de l'univers au fil du temps
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
        
        for p in population:
            p.gameDraw(self.screen,self.scale)
        
        
        self.screen.blit(text_surface_obj,(50,20))
        pygame.display.update()
        self.clock.tick(self.fps)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.run= False 
        
        self.gameKeys = pygame.key.get_pressed()
            

if __name__ == "__main__": 
    
    from vecteur3D import Vecteur3D
    from math import pi
    from pylab import plot, show, legend
    
    toto = Tortue()
    mario= Tortue(Vecteur3D(1,1),pi/2,name='mario',color='blue')
    
    toto.save()
    
    
    a = 1.5*pi 
    print (a,toPi(a))
    a = -1.5*pi 
    print (a,toPi(a))
    
    mick = Tortue(name='mick')
    mario.turn(pi)
    mario.walk(.5)
    mario.turn(-pi/4)
    mario.walk(.5)
    
    
    toto.turn(pi/4)
    toto.walk(1)
    

    toto.save()
    
    
    mick.load('toto')
    
    mick.plot()
    mario.plot()
    legend()
    show()
    
    
        
