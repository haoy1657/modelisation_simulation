import math
import pygame
import sys
from vecteur3D import Vecteur3D

# Define some constants
G = 9.81    # gravitational acceleration
DT = 0.01   # time step (s)

# Define the lengths of the pendulums (m)
L1 = 0.1
L2 = 0.2
L3 = 0.3

# Define the initial conditions
theta1 = math.pi / 4    # initial angle of pendulum 1 (rad)
theta2 = math.pi / 4    # initial angle of pendulum 2 (rad)
theta3 = math.pi / 4    # initial angle of pendulum 3 (rad)
omega1 = 0              # initial angular velocity of pendulum 1 (rad/s)
omega2 = 0              # initial angular velocity of pendulum 2 (rad/s)
omega3 = 0              # initial angular velocity of pendulum 3 (rad/s)

# Define the theoretical periods of the pendulums (s)
T1_theoretical = 2 * math.pi * math.sqrt(L1 / G)
T2_theoretical = 2 * math.pi * math.sqrt(L2 / G)
T3_theoretical = 2 * math.pi * math.sqrt(L3 / G)

# Initialize Pygame
pygame.init()

# Set up the window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pendulum Simulation")

# Set up the clock
clock = pygame.time.Clock()

# Define the function to update the pendulum angles and velocities
# Define the function to update the pendulum angles and velocities
def update_pendulum(theta, omega, L):
    # Calculate the angular acceleration
    alpha = -G / L * math.sin(theta.z)
    # Update the angular velocity and angle
    omega += Vecteur3D(0, 0, alpha) * DT   # Convert alpha to a Vecteur3D object
    theta += omega * DT
    # Return the updated angle and velocity
    return theta, omega

# Define the function to draw the pendulum
def draw_pendulum(theta, L, color):
    # Calculate the position of the pendulum bob
    x = L * math.sin(theta.z)
    y = L * math.cos(theta.z)
    # Draw the pendulum rod
    pygame.draw.line(screen, color, (400, 300), (400 + x * 100, y * 100 + 300), 2)
    # Draw the pendulum bob
    pygame.draw.circle(screen, color, (int(400 + x * 100), int(y * 100 + 300)), 10)

# Initialize the angles and velocities
theta1_vec = Vecteur3D(0, 0, theta1)
theta2_vec = Vecteur3D(0, 0, theta2)
theta3_vec = Vecteur3D(0, 0, theta3)
omega1_vec = Vecteur3D(0, 0, omega1)
omega2_vec = Vecteur3D(0, 0, omega2)
omega3_vec = Vecteur3D(0, 0, omega3)


# Main loop
font = pygame.font.SysFont('Arial', 20)
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update the pendulum angles and velocities
    theta1_vec, omega1_vec = update_pendulum(theta1_vec, omega1_vec, L1)
    theta2_vec, omega2_vec = update_pendulum(theta2_vec, omega2_vec, L2)
    theta3_vec, omega3_vec = update_pendulum(theta3_vec, omega3_vec, L3)

    # Draw the pendulums
    draw_pendulum(theta1_vec, L1, (255, 0, 0))
    draw_pendulum(theta2_vec, L2, (0, 255, 0))
    draw_pendulum(theta3_vec, L3, (0, 0, 255))

    # Calculate the periods of the pendulums (s)
    T1 = 2 * theta1_vec.z / omega1_vec.z
    T2 = 2 * theta2_vec.z / omega2_vec.z
    T3 = 2 * theta3_vec.z / omega3_vec.z

    # Print the periods of the pendulums and their theoretical periods
    print("Pendulum 1: period = {:.2f} s, theoretical period = {:.2f} s".format(T1, T1_theoretical))
    print("Pendulum 2: period = {:.2f} s, theoretical period = {:.2f} s".format(T2, T2_theoretical))
    print("Pendulum 3: period = {:.2f} s, theoretical period = {:.2f} s".format(T3, T3_theoretical))
    # Draw the text
    text1 = font.render("Pendulum 1: period = {:.2f} s, theoretical period = {:.2f} s".format(T1, T1_theoretical), True, (0, 0, 0))
    text2 = font.render("Pendulum 2: period = {:.2f} s, theoretical period = {:.2f} s".format(T2, T2_theoretical), True, (0, 0, 0))
    text3 = font.render("Pendulum 3: period = {:.2f} s, theoretical period = {:.2f} s".format(T3, T3_theoretical), True, (0, 0, 0))
    screen.blit(text1, (10, 50))
    screen.blit(text2, (10, 100))
    screen.blit(text3, (10, 150))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()