import pygame  # Import the pygame module
import sys  # Import the sys module for system-specific parameters and functions
import random  # Import the random module for generating random numbers
from vecteur3D import Vecteur3D  # Import the Vecteur3D class from the vecteur3D module

class Particle:
    def __init__(self, position, velocity, mass):
        # Initialize particle with its position, velocity and mass
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def update(self, dt):
        # Update the particle's position and velocity based on current velocity and acceleration
        self.position += self.velocity * dt
        self.velocity += self.acceleration() * dt

    def acceleration(self):
        # Calculate the total force on the particle
        force = self.gravity() + self.force_field()

        # Calculate the acceleration of the particle based on the total force and its mass
        acceleration = force * (1 / self.mass)

        return acceleration

    def gravity(self):
        # Calculate the gravitational force on the particle
        force = Vecteur3D(0, 0, -self.mass * 9.81)

        return force

    def force_field(self):
        # Calculate the force field force on the particle, which is a gravity-like force
        center = Vecteur3D(WIDTH / 2, HEIGHT / 2, -5)  # Use screen center as force field center
        displacement = center - self.position
        distance = displacement.mod()
        direction = displacement.norm()  # Take the opposite direction of displacement vector
        force = direction * (0.1 * self.mass * distance)

        return force


# Define constants
WIDTH = 1000  # Width of the screen in pixels
HEIGHT = 700  # Height of the screen in pixels
FPS = 60  # Number of frames per second
SIMULATION_TIME = 10.0  # Duration of the simulation, in seconds

# Initialize pygame
pygame.init()  # Initialize all imported pygame modules
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set the display size of the window
clock = pygame.time.Clock()  # Create an object to help track time

# Create particles
particles = []
for i in range(10):
    mass = random.uniform(0.1, 1.0)  # Generate a random mass for the particle
    x = random.uniform(0, WIDTH)  # Generate a random x-coordinate for the particle
    y = random.uniform(0, HEIGHT)  # Generate a random y-coordinate for the particle
    z = random.uniform(10, 20)  # Generate a random z-coordinate for the particle
    position = Vecteur3D(x, y, z)  # Create a vector representing the particle's position
    vx = random.uniform(-10, 10)  # Generate a random velocity in the x-direction for the particle
    vy = random.uniform(-10, 10)  # Generate a random velocity in the y-direction for the particle
    vz = random.uniform(-10, 10)  # Generate a random velocity in the z-direction for the particle
    velocity = Vecteur3D(vx, vy, vz)  # Create a vector representing the particle's velocity
    particle = Particle(position, velocity, mass)  # Create the particle
    particles.append(particle)  # Add the particle to the list of particles


# Start simulation loop
t = 0.0 #Initialize time to zero
dt = 1 / FPS  # Calculate the time step for each frame
# Initialize a while loop to run the simulation until the specified time is reached
while t < SIMULATION_TIME:
    # Handle Pygame events
    for event in pygame.event.get():
        # If the user clicks the window close button, exit the Pygame window and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the position of each particle using the specified time step
    for particle in particles:
        particle.update(dt)

    # Draw the particles on the Pygame screen
    screen.fill((255, 255, 255))
    for particle in particles:
        # Get the position and mass of the particle and calculate its size
        x, y, z = particle.position.x, particle.position.y, particle.position.z
        size = int(particle.mass * 10)
        # Draw a circle on the screen representing the particle, using its position, size, and color
        pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), size)

    # Draw a force field circle on the Pygame screen
    center = Vecteur3D(WIDTH / 2, HEIGHT / 2, -5)
    size = 100
    # Draw a circle on the screen representing the force field, using its position, size, and color
    pygame.draw.circle(screen, (255, 0, 0), (int(center.x), int(center.y)), size, 1)

    # Update the Pygame screen
    pygame.display.flip()
    # Wait for the specified number of frames per second to elapse before continuing the loop
    clock.tick(FPS)

    # Increment the time by the time step
    t += dt

# End the Pygame window and the program
pygame.quit()
sys.exit()
