import pygame

class Bird:
    def __init__(self):
        self.height = 0
    
    def draw(self, screen):
        # draw the bird
        pygame.draw.rect(screen, "yellow", (25, 360 - 25, 50, 50))