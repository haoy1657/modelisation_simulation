# Import necessary libraries
import pygame     # for graphics and user interaction
import sys        # for system-related tasks
import matplotlib.pyplot as plt   # for data visualization

# Constants
WIDTH = 800   # screen width
HEIGHT = 600  # screen height
DT = 0.010    # time step

# Initialize empty lists to store data
a = []   # acceleration
v = []   # velocity
y = []   # position
t = []   # time

# Mass-spring-damper system class
class MassSpringDamper:
    def __init__(self, mass, k, c, y0, v0, a0, f, t0):
        self.mass = mass  # mass of the object
        self.k = k        # spring constant
        self.c = c        # damping coefficient
        self.y = y0       # initial position
        self.v = v0       # initial velocity
        self.a = a0       # initial acceleration
        self.f = f        # external force
        self.t = t0       # initial time

    def update(self):
        # Calculate acceleration based on current position, velocity, and external force
        self.a = (9.81 + self.f - self.c * self.v - self.k * self.y) / self.mass
        # Update velocity and position based on current acceleration and time step
        self.v += self.a * DT
        self.y += self.v * DT
        self.t += DT
        # Append the updated data to the corresponding lists
        y.append(self.y)
        a.append(self.a)
        v.append(self.v)
        t.append(self.t)

    def draw(self, screen):
        # Draw the object as a red circle and display its current position, velocity, acceleration, and time
        font = pygame.font.SysFont('arial', 30)
        a_str = "{:.2f}".format(self.a)
        v_str = "{:.2f}".format(self.v)
        y_str = "{:.2f}".format(self.y)
        t_str = "{:.2f}".format(self.t)
        text = font.render("a: " + a_str, True, (0, 255, 0))
        text1 = font.render("v: " + v_str, True, (0, 255, 0))
        text2 = font.render("y: " + y_str, True, (0, 255, 0))
        text3 = font.render("t: " + t_str, True, (0, 255, 0))
        screen.blit(text, (15, 15))
        screen.blit(text1, (15, 60))
        screen.blit(text2, (15, 105))
        screen.blit(text3, (15, 145))
        pygame.draw.circle(screen, (255, 0, 0), (WIDTH // 2, int(self.y)), 20)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # create Pygame window
clock = pygame.time.Clock()

# Create mass-spring-damper system
mass = 2
k = 5
c = 1
y0 = 2 * HEIGHT // 3
v0 = 0
a0 = 0
f = 100
t0 = 0
msd = MassSpringDamper(mass, k, c, y0, v0, a0, f, t0)

# Simulation loop
while msd.t < 10: # while loop to continue simulation until t reaches 10
    # Handle events
    for event in pygame.event.get():# loop through all Pygame events
        if event.type == pygame.QUIT:# if user clicks the close button, exit program
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:# if user presses a key
            if event.key == pygame.K_q:# if the key is 'q', exit program
                pygame.quit()
                sys.exit()

    # Update mass-spring-damper system and get acceleration
    msd.update() # update the state of the system

    # Draw mass-spring-damper system
    screen.fill((255, 255, 255))# fill the screen with white
    msd.draw(screen)# draw the system on the screen
    pygame.display.update()# update the display

    # Wait for next frame
    clock.tick(60)# limit the frame rate to 60 FPS

# Close the Pygame window and show Matplotlib plot
pygame.quit() # close the Pygame window
fig, ax = plt.subplots(visible=True) # create a new figure and axis for Matplotlib plot
ax.plot(t, a, label='Acceleration') # plot acceleration vs. time
ax.plot(t, y, label='Position') # plot position vs. time
ax.plot(t, v, label='Velocity') # plot velocity vs. time
ax.set_xlabel('t') # set x-axis label to 't'
plt.legend() # show the legend
plt.show(block=True) # show the plot and block program until plot is closed
