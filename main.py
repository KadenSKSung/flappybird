import pygame
from Bird import Bird
from Pipe import Pipe

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# game setup
bird = Bird()
pipe = Pipe(200)
pipe2 = Pipe(600)
pipe3 = Pipe(1000)
pipe4 = Pipe(1400)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#6ac8f5")

    # RENDER YOUR GAME HERE
    bird.draw(screen)
    bird.apply_velocity()
    pipe.draw(screen)
    pipe2.draw(screen)
    pipe3.draw(screen)
    pipe4.draw(screen)
    pipe.move()
    pipe2.move()
    pipe3.move()
    pipe4.move()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()