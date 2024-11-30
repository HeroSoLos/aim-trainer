import random
import math
import pygame


class Cursor:
    def __init__(self, position, health, mana, passive_buffs=None, spell_order=None, current_spell=0) -> None:
        if spell_order is None:
            spell_order = []

        if passive_buffs is None:
            passive_buffs = []

        self.position = position
        self.health = health
        self.mana = mana
        self.passive_buffs = passive_buffs
        self.spell_order = spell_order
        self.current_spell = current_spell

        # Inventory variables
        self.inventory_x_offset = 25
        self.image_side_length = 50
        self.binding_box_width = 3
        self.displayed_spells = 3
        self.active_box_width = 5
        self.nonactive_opacity = 150
        self.inventory_repeat_draw = 0
        self.INVENTORY_REPEAT = 120
        self.fade_away_opacity1 = 100
        self.fade_away_opacity2 = 50
        # Key Interaction Variables
        self.key_hold_delay = 0
        self.KEY_HOLD_REPEAT = 20
        #DEMO VARIABLES:
        self.square_repeat_draw = 0
        self.triangle_repeat_draw = 0
        self.hexagon_repeat_draw = 0
        self.angle = 0

    def __str__(self):
        return f"Cursor({self.position})"

    def draw_cursor(self, screen):
        pass #TODO: add cursor

    def draw_spell_inventory(self, screen):
        self.draw_inventory_opacity_change(screen, self.nonactive_opacity)

        previousSpell = self.current_spell-1
        nextSpell = self.current_spell+1
        if previousSpell < 0:
            previousSpell = len(self.spell_order)-1
        if  nextSpell >= len(self.spell_order):
            nextSpell = 0

        previousSpellImage = self.spell_order[previousSpell].image.copy()
        previousSpellImage.set_alpha(self.nonactive_opacity)
        nextSpellImage = self.spell_order[nextSpell].image.copy()
        nextSpellImage.set_alpha(self.nonactive_opacity)

        screen.blit(previousSpellImage, (self.position[0]+self.inventory_x_offset, self.position[1]-(self.displayed_spells*self.image_side_length/2)))
        screen.blit(self.spell_order[self.current_spell].image, (self.position[0]+self.inventory_x_offset, self.position[1]-(self.image_side_length/2)))
        screen.blit(nextSpellImage, (self.position[0]+self.inventory_x_offset, self.position[1]+(self.image_side_length/2)))

        pygame.draw.rect(screen, (50, 50, 50), (self.position[0]+self.inventory_x_offset, self.position[1]-(self.displayed_spells*self.image_side_length/2), self.image_side_length, self.displayed_spells*self.image_side_length), self.binding_box_width)
        pygame.draw.rect(screen, (0, 0, 0), (self.position[0]+self.inventory_x_offset, self.position[1]-(self.image_side_length/2), self.image_side_length, self.image_side_length), self.active_box_width)
        """for i, spell in enumerate(self.spell_order):
            if i == self.current_spell:
                pygame.draw.rect(screen, (255, 0, 0), (100 * i, 500, 100, 50))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (100 * i, 500, 100, 50))
            screen.blit(spell.image, (100 * i + 10, 500 + 10))"""

    def draw_inventory_opacity_change(self, screen, opacity):
        temp_surface = pygame.surface.Surface((self.image_side_length, self.image_side_length * self.displayed_spells), pygame.SRCALPHA)
        temp_surface.fill((50, 50, 50, opacity))
        screen.blit(temp_surface, (self.position[0] + self.inventory_x_offset, self.position[1] - (self.displayed_spells * self.image_side_length / 2)))

    def cycle_spell_forward(self):
        self.current_spell += 1
        if self.current_spell >= len(self.spell_order):
            self.current_spell = 0

    def cycle_spell_backward(self):
        self.current_spell -= 1
        if self.current_spell < 0:
            self.current_spell = len(self.spell_order) - 1

    def cast_spell(self):
        pass # return self.spell_order[current_spell]

    def set_position(self, mouse_position):
        self.position = mouse_position

    # DEMO FUNCTIONS
    def draw_rect(self, screen):
        if self.square_repeat_draw > 0:
            side_length = 100  # Constant side length of the square
            mouse_x, mouse_y = self.position  # Get current mouse position
            half_diagonal = math.sqrt(2 * (side_length / 2) ** 2)
            angle = math.radians(self.angle)
            vertices = []
            for i in range(4):
                theta = angle + i * math.pi / 2
                x = mouse_x + half_diagonal * math.cos(theta)
                y = mouse_y + half_diagonal * math.sin(theta)
                vertices.append((x, y))
            pygame.draw.polygon(screen, (255, 0, 0), vertices, 3)  # Drawing a red square
        self.square_repeat_draw -= 1

    def draw_triangle(self, screen):
        side_length = 150  # Constant side length of the triangle
        mouse_x, mouse_y = self.position  # Get current mouse position
        height = (math.sqrt(3) / 2) * side_length
        vertices = []
        angles = [0, 2 * math.pi / 3, 4 * math.pi / 3]
        for a in angles:
            x = mouse_x + height * math.cos(math.radians(self.angle) + a)
            y = mouse_y + height * math.sin(math.radians(self.angle) + a)
            vertices.append((x, y))
        pygame.draw.polygon(screen, (0, 0, 255), vertices, 3)  # Blue triangle

    def draw_hexagon(self, screen):
        radius = 125  # Constant radius of the hexagon
        mouse_x, mouse_y = self.position  # Get current mouse position
        points = []
        for i in range(6):
            angle = self.angle + i * (2 * math.pi / 6)
            x = mouse_x + radius * math.cos(angle)
            y = mouse_y + radius * math.sin(angle)
            points.append((x, y))
        return pygame.draw.polygon(screen, (0, 255, 0), points, 3) # Green hexagon

        
    def check_hexagon_collide(self, targetList, hexagon, screenWidth, screenHeight):
        for target in targetList:  # Check if hit
            if target.rect.colliderect(hexagon):  # Hit target
                target.clicked(screenWidth, screenHeight)

    def update_angle(self):
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0



