import pygame
import random

PIPE_GAP = 180
PIPE_LIP_WIDTH = 100
PIPE_LIP_HEIGHT = 25
PIPE_WIDTH = 80

colors = ["red", "yellow", "green", "blue", "orange"]


class Pipe:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(100, 620)
        self.color = random.choice(colors)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (
            self.x - PIPE_LIP_WIDTH / 2,
            self.y - PIPE_GAP / 2 - PIPE_LIP_HEIGHT,
            PIPE_LIP_WIDTH,
            PIPE_LIP_HEIGHT
        ))

        pygame.draw.rect(screen, self.color, (
            self.x - PIPE_WIDTH / 2,
            0,
            PIPE_WIDTH,
            self.y - PIPE_GAP / 2 - PIPE_LIP_HEIGHT
        ))

        pygame.draw.rect(screen, self.color, (
            self.x - PIPE_LIP_WIDTH / 2,
            self.y + PIPE_GAP / 2,
            PIPE_LIP_WIDTH,
            PIPE_LIP_HEIGHT
        ))

        pygame.draw.rect(screen, self.color, (
            self.x - PIPE_WIDTH / 2,
            self.y + PIPE_GAP / 2 + PIPE_LIP_HEIGHT, 
            PIPE_WIDTH,
            720 - (self.y + PIPE_GAP / 2 + PIPE_LIP_HEIGHT)
        ))
    
    def move(self):
        self.x -= 3

        if self.x < -PIPE_LIP_WIDTH:
            self.x = 1282 + PIPE_LIP_WIDTH
            self.color = random.choice(colors)
    
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