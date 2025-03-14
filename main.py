import pygame
from Bird import Bird
from Pipe import Pipe

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font100 = pygame.font.SysFont("Arial", 100)
font60 = pygame.font.SysFont("Arial", 60)
font30 = pygame.font.SysFont("Arial", 30)
running = True


# texts
text_gameover = font100.render("Game Over", True, "red")
text_gameover_pos = (640 - text_gameover.get_width()/2, 360 - text_gameover.get_height()/2)
text_scoreboard = font30.render("0", True, "black")
text_scoreboard_pos = (1270 - text_scoreboard.get_width(), 10)
text_again = font60.render("Play Again", True, "black")
text_again_pos = (640 - text_again.get_width()/2, 490 - text_gameover.get_height()/2)

# game setup
bird_alive = True
started = False
bird = Bird()
pipes = [
    Pipe(602),
    Pipe(1001),
    Pipe(1400),
    Pipe(1760),
]
score = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True
                bird.jump()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#6ac8f5")

    # RENDER YOUR GAME HERE
    if bird.collides_with(pipes):
        bird_alive = False

    for pipe in pipes:
        pipe.draw(screen)
        if started and bird_alive:
            pipe.move()
        if pipe.x == 50 and bird_alive:
            score += 1
    

    if bird_alive:
        bird.draw(screen)
        if started:
            bird.apply_velocity()
    else:
        screen.blit(text_gameover, text_gameover_pos)
        screen.blit(text_again, text_again_pos)
    
    screen.blit(text_scoreboard, text_scoreboard_pos)

    text_scoreboard = font30.render(str(score), True, "black")
    text_scoreboard_pos = (1270 - text_scoreboard.get_width(), 10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()