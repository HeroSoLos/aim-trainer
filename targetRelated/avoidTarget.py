import random
import math
from targetRelated.target import Target

class AvoidTarget(Target):
    def __init__(self, index, position, direction, speed, acceleration, color, image, radius, change_ratio=0.5):
        super().__init__(index, position, direction, speed, acceleration, color, image)
        self.radius = radius
        self.change_ratio = change_ratio

    def __str__(self):
        return f"AvoidTarget({self.index})"

    def calculate_direction(self, mouse_position, screen_width, screen_height):
        displacement_x = self.position[0] - mouse_position[0]
        displacement_y = self.position[1] - mouse_position[1]
        distance = math.sqrt(displacement_y**2 + displacement_x**2)
        # screen_diagonal_distance = math.sqrt(screen_height**2 + screen_width**2)
        
        self.direction[0] = displacement_x / screen_width
        self.direction[1] = displacement_y / screen_height
        
        if distance < self.radius: # four to split into 4 parts on the diag
            pass
        elif distance > self.radius:
            self.direction[0] *= -1
            self.direction[1] *= -1
        else:
            self.direction[0] = 0
            self.direction[1] = 0
        
        
        
    def check_wall_collision(self, screen_width, screen_height):
        if self.position[0] > (screen_width - self.rect.width) and self.direction[0] > 0:
            self.direction[0] = 0
        elif self.position[0] < 0 and self.direction[0] < 0:
            self.direction[0] = 0
        if self.position[1] > (screen_height - self.rect.height) and self.direction[1] > 0:
            self.direction[1] = 0
        elif self.position[1] < 0 and self.direction[1] < 0:
            self.direction[1] = 0
