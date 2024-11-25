import random

class Target:
    def  __init__(self, index: int, position: list[2], direction: list[2], speed: int, color: list[3], image):
        self.index = index
        self.position = position
        self.direction = direction
        self.speed = speed
        self.color = color
        self.image = image

        self.rect = self.image.get_rect()

    def __str__(self):
        return f"Target({self.index})"

    def return_position(self):
        return self.position

    def move(self):
        self.position[0] += self.direction[0]*self.speed
        self.position[1] += self.direction[1]*self.speed

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def set_speed(self, speed):
        self.speed = speed

    def clicked(self, screen_width, screen_height):
        self.position = [random.randint(self.rect.width, screen_width - self.rect.width), random.randint(self.rect.height, screen_height - self.rect.height)]

    def check_wall_collision(self, screen_width, screen_height):
        if self.position[0] > screen_width or self.position[0] < 0:
            self.direction[0] *= -1
        elif self.position[1] > screen_height or self.position[1] < 0:
            self.direction[1] *= -1