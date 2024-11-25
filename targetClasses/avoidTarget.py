import random
from targetClasses.target import Target

class AvoidTarget(Target):
    def __init__(self, index, position, direction, speed, color, image, change_ratio=0.5):
        super().__init__(index, position, direction, speed, color, image)
        self.change_ratio = change_ratio

    def __str__(self):
        return f"AvoidTarget({self.index})"

    def calculate_direction(self, mouse_position, screen_width, screen_height):
        self.direction[0] = (self.position[0] - mouse_position[0])/screen_width
        self.direction[1] = (self.position[1] - mouse_position[1])/screen_height

    def check_wall_collision(self, screen_width, screen_height):
        if self.position[0] > (screen_width - self.rect.width) or self.position[0] < 0:
            self.direction[0] = 0
        if self.position[1] > (screen_height - self.rect.height) or self.position[1] < 0:
            self.direction[1] = 0
