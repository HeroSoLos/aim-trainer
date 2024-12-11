import pygame

class VoidSpell:
    def __init__(self, level = 50, cool_down = 10):
        self.image_path = r"assets/spellIcons/void_spell2.jpg"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
        # Scalable variables
        self.level = level
        self.cool_down = cool_down
        self.COOL_DOWN_RESET = 10

        # Draw things:
        self.draw_at = [0, 0]
    def cast(self, screen, mouse_pos, target_list):
        pygame.draw.circle(screen, (0, 0, 0), mouse_pos, self.level)
        targets_to_click = []
        for target in target_list:
            dx = target.rect.centerx - mouse_pos[0]
            dy = target.rect.centery - mouse_pos[1]
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance <= self.level:
                targets_to_click.append(target)

        print("Casting void spell with image:", self.image_path)
        return targets_to_click
