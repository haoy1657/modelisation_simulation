import pygame # Pygame is a library used to create games and multimedia applications
import sys # sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
import math # Math module provides access to the mathematical functions defined by the C standard
from vecteur3D import Vecteur3D # Importing a class named Vecteur3D from a module named vecteur3D

# Constants
WIDTH = 800 # Width of the game window
HEIGHT = 600 # Height of the game window
G = 9.81 # Acceleration due to gravity
L1 = 15 # Length of the first pendulum arm
L2 = 10 # Length of the second pendulum arm
M1 = 2 # Mass of the first pendulum bob
M2 = 1 # Mass of the second pendulum bob
DT = 0.01 # Time step for simulation
# Double pendulum class
class DoublePendulum:
    def __init__(self, theta1, theta2, omega1, omega2):
        # Initialize angles and angular velocities
        self.theta1 = theta1 + math.pi  
        self.theta2 = theta2 + math.pi  
        self.omega1 = omega1
        self.omega2 = omega2


    def update(self):
        # Calculate accelerations
        delta = self.theta2 - self.theta1  # Difference in angles
        den1 = (M1 + M2) * L1 - M2 * L1 * math.cos(delta) * math.cos(delta)  # Common denominator for acc1 and acc2
        den2 = L2 * L2 * (M1 + M2 - M2 * math.cos(delta) * math.cos(delta))  # Common denominator for acc1 and acc2
        omega1_sq = self.omega1 * self.omega1  # Square of angular velocity of first pendulum bob
        omega2_sq = self.omega2 * self.omega2  # Square of angular velocity of second pendulum bob
        num1 = -M2 * L1 * omega1_sq * math.sin(delta) - (M1 + M2) * G * math.sin(self.theta1)  # Numerator for acc1
        num2 = L2 * omega2_sq * math.sin(delta) - G * math.sin(self.theta2)  # Numerator for acc2
        acc1 = (num1 * den2 - num2 * M2 * L1 * math.cos(delta)) / (den1 * den2 - M2 * L1 * L2 * math.cos(delta) * math.cos(delta))  # Acceleration of first pendulum bob
        acc2 = (num2 * den1 - num1 * M2 * L2 * math.cos(delta)) / (den1 * den2 - M2 * L1 * L2 * math.cos(delta) * math.cos(delta))  # Acceleration of second pendulum bob
    
        # Update angles and angular velocities
        self.theta1 += self.omega1 * DT
        self.theta2 += self.omega2 * DT
        self.omega1 += acc1 * DT
        self.omega2 += acc2 * DT
    
    def get_positions(self):
        # Calculate positions of pendulum masses
        x1 = L1 * math.sin(self.theta1)  # X-coordinate of first pendulum bob
        y1 = L1 * math.cos(self.theta1)  # Y-coordinate of first pendulum bob
        x2 = x1 + L2 * math.sin(self.theta2)  # X-coordinate of second pendulum bob
        y2 = y1 + L2 * math.cos(self.theta2)  # Y-coordinate of second pendulum bob
        return (Vecteur3D(x1, y1, 0), Vecteur3D(x2, y2, 0))  # Return tuple of positions as 3D vectors


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# Create double pendulum
dp = DoublePendulum(math.pi/2, math.pi/2, 0, 0)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        # If user quits game, exit the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update double pendulum
    dp.update()

    # Draw double pendulum
    # Set background color to white
    screen.fill((255, 255, 255))
    # Get the positions of the pendulum's masses
    (pos1, pos2) = dp.get_positions()
    # Draw the first pendulum mass and rod
    pygame.draw.line(screen, (255, 0, 0), (WIDTH/2, HEIGHT/2), (pos1.x + WIDTH/2, pos1.y + HEIGHT/2), 3)
    pygame.draw.circle(screen, (255, 0, 0), (int(pos1.x + WIDTH/2), int(pos1.y + HEIGHT/2)), 10)
    # Draw the second pendulum mass and rod
    pygame.draw.line(screen, (0, 0, 255), (pos1.x + WIDTH/2, pos1.y + HEIGHT/2), (pos2.x + WIDTH/2, pos2.y + HEIGHT/2), 3)
    pygame.draw.circle(screen, (0, 0, 255), (int(pos2.x + WIDTH/2), int(pos2.y + HEIGHT/2)), 10)
    # Update the game window
    pygame.display.update()

    # Wait for next frame
    clock.tick(60)