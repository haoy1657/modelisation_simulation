# Import required libraries
import pygame
import sys
import math
from vecteur3D import Vecteur3D

# Constants
WIDTH = 800
HEIGHT = 600
M1 = 1
M2 = 1
K1 = 1
K2 = 1
K3 = 1
L1 = 10
L2 = 20
L3 = 10
DT = 0.01

# 2DOF system class
class TwoDOFSystem:
    def __init__(self, x1, x2, v1, v2):
        """
        Initialize TwoDOFSystem object.

        Args:
            x1 (float): initial displacement of mass 1 in radians.
            x2 (float): initial displacement of mass 2 in radians.
            v1 (float): initial velocity of mass 1.
            v2 (float): initial velocity of mass 2.
        """
        self.x1 = x1
        self.x2 = x2
        self.v1 = v1
        self.v2 = v2
    
    def update(self):
        """
        Update the state of the 2DOF system by calculating the accelerations and updating the positions and velocities of masses 1 and 2.
        """
        # Calculate accelerations
        a1 = (-K1 * self.x1 + K2 * (self.x2 - self.x1) + K3 * self.x2) / M1
        a2 = (K3 * (self.x1 - self.x2) - K2 * self.x2) / M2
        
        # Update positions and velocities
        self.x1 += self.v1 * DT
        self.x2 += self.v2 * DT
        self.v1 += a1 * DT
        self.v2 += a2 * DT
    
    def get_positions(self):
        """
        Calculate the positions of masses 1 and 2.

        Returns:
            tuple: A tuple of two Vecteur3D objects representing the positions of masses 1 and 2.
        """
        # Calculate positions of masses
        pos1 = Vecteur3D(L1 * math.sin(self.x1), 0, 0)
        pos2 = Vecteur3D(L1 * math.sin(self.x1) + L2 * math.sin(self.x2), 0, 0)
        
        return (pos1, pos2)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create 2DOF system
in_phase = TwoDOFSystem(0, 0, 0, 0)
out_of_phase = TwoDOFSystem(math.pi/2, -math.pi/2, 0, 0)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update systems
    in_phase.update()
    out_of_phase.update()
    
    # Draw systems
    # Fill the screen with white color
    screen.fill((255, 255, 255))
    
    # Get the positions of the pendulums in the in-phase system
    (pos1, pos2) = in_phase.get_positions()
    
  
    # Get the positions of the pendulums in the out-of-phase system
    (pos1, pos2) = out_of_phase.get_positions()
    

    pygame.draw.line(screen, (255, 0, 0), (WIDTH/2, HEIGHT/2), (pos1.x + WIDTH/2, pos1.y + HEIGHT/2), 3)
    pygame.draw.circle(screen, (255, 0, 0), (int(pos1.x + WIDTH/2), int(pos1.y + HEIGHT/2)), 10)
    

    pygame.draw.line(screen, (0, 0, 255), (pos1.x + WIDTH/2, pos1.y + HEIGHT/2), (pos2.x + WIDTH/2, pos2.y + HEIGHT/2), 3)
    pygame.draw.circle(screen, (0, 0, 255), (int(pos2.x + WIDTH/2), int(pos2.y + HEIGHT/2)), 10)
    #Draw the first spring of the out-of-phase system as a green line
    pygame.draw.line(screen, (0, 255, 0), (WIDTH/2, HEIGHT/2), (pos1.x + WIDTH/2 - L1, pos1.y + HEIGHT/2), 3)
    #Draw the second spring of the out-of-phase system as a green line
    pygame.draw.line(screen, (0, 255, 0), (pos1.x + WIDTH/2 - L1, pos1.y + HEIGHT/2), (pos2.x + WIDTH/2 - L3, pos2.y + HEIGHT/2), 3)
    #Draw the third spring of the out-of-phase system as a green line
    pygame.draw.line(screen, (0, 255, 0), (pos2.x + WIDTH/2 - L3, pos2.y + HEIGHT/2), (pos2.x + WIDTH/2, pos2.y + HEIGHT/2), 3)

    # Update display
    pygame.display.update()
    #Tick the clock to control the frame rate
    clock.tick(60)