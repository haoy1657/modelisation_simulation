import pygame
from pygame.locals import *

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

W = 720
H = 480

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
size = 16

def trace_rect(P1,P2):
    size=16
    return pygame.draw.rect(screen,RED,(P1-size/2,P2-size/2,size,size),5)

def trace_circle(P1,P2):
    size=16
    return pygame.draw.circle(screen,BLUE,(P1,P2),16,5)
    
    
P1 = 50
P2 = 50
running = True

while running:
    clock.tick(FPS)
    
    pygame.event.pump() # process event queue
    keys = pygame.key.get_pressed() # It gets the states of all keyboard keys.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    if keys[ord('z')] or keys[pygame.K_UP]: # And if the key is K_DOWN:
        P2 -= 5
    if keys[ord('s')] or keys[pygame.K_DOWN]: # And if the key is K_DOWN:
        P2 += 5
    if keys[ord('q')] or keys[pygame.K_LEFT]: # And if the key is K_DOWN:
        P1 -= 5
    if keys[ord('d')] or keys[pygame.K_RIGHT]: # And if the key is K_DOWN:
        P1 += 5
    
    screen.fill(BLACK)
    #pygame.draw.rect(screen,RED,(P1-size,P2-size,P1+size,P2+size),2)

    trace_rect(P1,P2)
    
    trace_circle(P1,P2)
    
    pygame.draw.line(screen,GREEN,(H/2,W/2),(P1,P2),2)
    
    pygame.display.update()  # Or pygame.display.flip()

    if keys[pygame.K_ESCAPE]:
        running = False
        pygame.quit()

quit()    
