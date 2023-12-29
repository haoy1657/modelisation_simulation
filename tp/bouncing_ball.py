import sys, pygame

pygame.init() # initialisation de l'écran de jeu 


size = width, height = 400,300 # taille de la fenêtre

speed = [2, 2] #vitesse balle

white = [255, 255, 255]  


screen = pygame.display.set_mode(size)


ball = pygame.image.load("balle-rebondissante.png")
# Redimensionner l'image
new_size = (ball.get_width() // 20, ball.get_height() // 20)
ball = pygame.transform.scale(ball, new_size)


ballrect = ball.get_rect()

clock = pygame.time.Clock()

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()


    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:

        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:

        speed[1] = -speed[1]


    screen.fill(white)

    screen.blit(ball, ballrect)

    clock.tick(60)
    pygame.display.flip()

