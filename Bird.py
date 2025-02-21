import pygame

class Bird:
    def __init__(self):
        self.height = 360
        self.velocity = 0
    
    def draw(self, screen):
        # draw the bird
        pygame.draw.circle(screen, "yellow", (50, 720 - self.height), 25)
    
    def apply_velocity(self):
        self.height += self.velocity
        self.velocity -= 0.175
        
        if self.height < 25:
            self.velocity = 0
            self.height = 25
        
        elif self.height > 695:
            self.velocity = 0
            self.height = 695
    
    def jump(self):
        self.velocity = 5
