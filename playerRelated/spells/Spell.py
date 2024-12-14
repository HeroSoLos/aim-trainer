import pygame

class Spell:
    def __init__(self, level=50, cool_down=10, image_path=""):
        self.level = level
        self.cool_down = cool_down
        self.COOL_DOWN_RESET = cool_down
        self.image_path = image_path
        if self.image_path:
            self.image = pygame.image.load(self.image_path)
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
        else:
            self.image = None
            self.rect = None
        self.draw_at = [0, 0]

    def cast(self, screen, mouse_pos, target_list):
        raise NotImplementedError("Subclasses must implement this method")