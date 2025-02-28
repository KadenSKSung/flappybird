import pygame
import random

PIPE_GAP = 180
PIPE_LIP_WIDTH = 100
PIPE_LIP_HEIGHT = 25
PIPE_WIDTH = 80

class Pipe:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(100, 620)

    def draw(self, screen):
        pygame.draw.rect(screen, "green", (
            self.x - PIPE_LIP_WIDTH / 2,
            self.y - PIPE_GAP / 2 - PIPE_LIP_HEIGHT,
            PIPE_LIP_WIDTH,
            PIPE_LIP_HEIGHT
        ))

        pygame.draw.rect(screen, "green", (
            self.x - PIPE_WIDTH / 2,
            0,
            PIPE_WIDTH,
            self.y - PIPE_GAP / 2 - PIPE_LIP_HEIGHT
        ))

        pygame.draw.rect(screen, "green", (
            self.x - PIPE_LIP_WIDTH / 2,
            self.y + PIPE_GAP / 2,
            PIPE_LIP_WIDTH,
            PIPE_LIP_HEIGHT
        ))

        pygame.draw.rect(screen, "green", (
            self.x - PIPE_WIDTH / 2,
            self.y + PIPE_GAP / 2 + PIPE_LIP_HEIGHT, 
            PIPE_WIDTH,
            720 - (self.y + PIPE_GAP / 2 + PIPE_LIP_HEIGHT)
        ))
    
    def move(self):
        self.x -= 3

        if self.x < -PIPE_LIP_WIDTH:
            self.x = 1280 + PIPE_LIP_WIDTH
    
    def get_hitbox(self):
        return (
            (
                self.x - PIPE_WIDTH / 2,
                0,
                PIPE_WIDTH,
                self.y - PIPE_GAP / 2
            ),
            (
                self.x - PIPE_WIDTH / 2,
                self.y + PIPE_GAP / 2,
                PIPE_WIDTH,
                720 - (self.y + PIPE_GAP / 2)
            )
        )