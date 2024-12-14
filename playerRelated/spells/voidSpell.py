import pygame
from spells import Spell

class VoidSpell(Spell):
    def __init__(self, level=50, cool_down=10):
        super().__init__(level, cool_down, image_path=r"assets/spellIcons/void_spell2.jpg")

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
