# Import the necessary libraries
import pygame
import sys
from random import uniform
from vecteur3D import Vecteur3D

# Define the dimensions of the screen where the simulation takes place
width = 1000
height = 700

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define the range of initial positions and velocities for the particle
pos_range = (0, width), (0, height), 0
vel_range = (-100, 100), (-200, 0), 0

# Define the particle parameters
radius = 5  # radius of the particle circle
color = (255, 255, 255)  # color of the particle circle
mass = 1.0  # mass of the particle

# Define the simulation parameters
dt = 0.01  # time step
gravity = Vecteur3D(0, 0, -9.81)  # downward force
viscosity = 0.1  # drag force coefficient

# Define the new `__truediv__` method in the `Vecteur3D` class
def __truediv__(self, scalar):
    return Vecteur3D(self.x / scalar, self.y / scalar, self.z / scalar)

Vecteur3D.__truediv__ = __truediv__

# Initialize the particle position and velocity
pos = Vecteur3D(uniform(*pos_range[0]), uniform(*pos_range[1]), 0)
vel = Vecteur3D(uniform(*vel_range[0]), uniform(*vel_range[1]), 0)

while True:
    # Handle events
    for event in pygame.event.get():  # Loop through all events in the event queue
        if event.type == pygame.QUIT:  # If the user clicks the close button
            pygame.quit()  # Stop the Pygame engine
            sys.exit()  # Close the window and quit the program
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # If the user presses the spacebar
            # Create a new particle with random position and velocity
            pos = Vecteur3D(uniform(*pos_range[0]), uniform(*pos_range[1]), 0)
            vel = Vecteur3D(uniform(*vel_range[0]), uniform(*vel_range[1]), 0)

    # Apply gravity and viscosity
    drag = viscosity * vel.norm() * vel.mod()  # Calculate the drag force
    acc = gravity + (drag / mass)  # Calculate the acceleration
    vel = vel + acc * dt  # Update the velocity
    pos = pos + vel * dt  # Update the position

    # Draw the particle on the screen
    screen.fill((0, 0, 0))  # Clear the screen
    font = pygame.font.SysFont('arial', 30)
    text = font.render("Press the spacebar to generate a new particle.", True, (0, 255, 0))  # Create a text object to display instructions
    screen.blit(text, (15, 15))  # Display the instructions on the screen
    pygame.draw.circle(screen, color, (int(pos.x), int(pos.y)), radius)  # Draw the particle as a circle on the screen
    pygame.display.update()  # Update the display

    clock.tick(60)  # Limit the frame rate to 60 fps using the Pygame clock object
