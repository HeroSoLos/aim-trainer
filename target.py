class Target:
    def  __init__(self, index: int, position: list[2], speed: list[2], color: list[3], image):
        self.index = index
        self.position = position
        self.color = color
        self.speed = speed
        self.image = image

    def __str__(self):
        return f"Target({self.index})"

    def return_position(self):
        return self.position

    def move(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def set_speed(self, speed):
        self.speed = speed

