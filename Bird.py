import pygame

BIRD_RADIUS = 25
BIRD_VELOCITY = 0.175
BIRD_HEIGHT = 695

class Bird:
    def __init__(self):
        self.height = 360
        self.velocity = 0
    
    def draw(self, screen):
        # draw the bird
        pygame.draw.circle(screen, "yellow", (50, 720 - self.height), BIRD_RADIUS)
    
    def apply_velocity(self):
        self.height += self.velocity
        self.velocity -= BIRD_VELOCITY
        
        if self.height < BIRD_RADIUS:
            self.velocity = 0
            self.height = BIRD_RADIUS
        
        elif self.height > BIRD_HEIGHT:
            self.velocity = 0
            self.height = BIRD_HEIGHT
    
    def jump(self):
        self.velocity = 5
