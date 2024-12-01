import pygame
class SummoningSpell:
    def __init__(self):
        self.image_path = r"assets/spellIcons/summoning_spell1.jpg"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
    def cast(self):
        # Template for casting the spell
        print("Casting summoning spell with image:", self.image_path)
