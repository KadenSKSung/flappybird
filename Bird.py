import pygame
import math

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
    
    def collides_with(self, pipes):
        for theta in range(-45, 225):
            # convert to radians
            theta = (theta * math.pi) / 180

            xdelta = BIRD_RADIUS * math.sin(theta)
            ydelta = BIRD_RADIUS * math.cos(theta)

            px = 50 + xdelta
            py = 720 - self.height + ydelta

            for pipe in pipes:
                h1, h2 = pipe.get_hitbox()

                x, y, w, h = h1
                if (
                    px > x and
                    py > y and
                    px < x + w and
                    py < y + h
                ):
                    return True
                
                x, y, w, h = h2
                if (
                    px > x and
                    py > y and
                    px < x + w and
                    py < y + h
                ):
                    return True
        return False