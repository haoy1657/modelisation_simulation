# -*- coding: utf-8 -*-
import sys
import pygame
import math

pygame.init()

# Dimensions de la fenêtre
size = width, height = 640, 480

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)

# Paramètres physiques de la pendule
g = 9.81  # Accélération gravitationnelle
L = 100.0  # Longueur du pendule
k = 10.0  # Coefficient de raideur du ressort
m = 1.0  # Masse de la boule

# Position initiale du pendule
theta0 = math.pi / 4  # Angle initial
x0 = width / 2  # Position horizontale initiale
y0 = height / 2  # Position verticale initiale
v0 = 0.0  # Vitesse initiale

# Initialisation des variables
theta = theta0
x = x0
y = y0
v = v0
dt = 0.01  # Intervalle de temps entre chaque itération

# Création de la fenêtre
screen = pygame.display.set_mode(size)

# Chargement de l'image de la boule
ball = pygame.image.load("balle-rebondissante.png")
# Redimensionner l'image
new_size = (ball.get_width() // 20, ball.get_height() // 20)
ball = pygame.transform.scale(ball, new_size)
ballrect = ball.get_rect()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcul des forces
    f_spring = -k * (L - y)  # Force du ressort
    f_gravity = m * g * math.sin(theta)  # Force gravitationnelle

    # Calcul des accélérations
    a_spring = f_spring / m
    a_gravity = f_gravity / m

    # Mise à jour des vitesses
    v += (a_spring + a_gravity) * dt

    # Mise à jour des positions
    x += v * math.sin(theta) * dt
    y += v * math.cos(theta) * dt
    theta += v / L * dt
    
    # Calcul de la position de la masse en bas
    ball_x = x - L * math.sin(theta)
    ball_y = y + L * math.cos(theta)


    # Affichage de la boule
    ballrect.centerx = x
    ballrect.centery = y
    screen.fill(black)
    screen.blit(ball, ballrect)

    # Affichage du ressort
    pygame.draw.line(screen, white, (x, y), (x, y + L), 2)

    # Affichage de la masse
    pygame.draw.circle(screen, white, (int(x), int(y)), 10)

    # Mise à jour de la fenêtre
    pygame.display.flip()

    # Attente avant la prochaine itération
    pygame.time.wait(10)
