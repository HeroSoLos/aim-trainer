import random
import math
import pygame


class Cursor:
    def __init__(self, position, health, mana, passive_buffs=None, spell_order=None) -> None:
        if spell_order is None:
            spell_order = []
        if passive_buffs is None:
            passive_buffs = []

        self.position = position
        self.health = health
        self.mana = mana
        self.passive_buffs = passive_buffs
        self.spell_order = spell_order
        self.current_spell = 0

        #DEMO VARIABLES:
        self.square_repeat_draw = 0
        self.triangle_repeat_draw = 0
        self.hexagon_repeat_draw = 0
        self.angle = 0

    def __str__(self):
        return f"Cursor({self.position})"

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
        if self.triangle_repeat_draw > 0:
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
        self.triangle_repeat_draw -= 1
    def draw_hexagon(self, screen):
        if self.hexagon_repeat_draw > 0:
            radius = 125  # Constant radius of the hexagon
            mouse_x, mouse_y = self.position  # Get current mouse position
            points = []
            for i in range(6):
                angle = self.angle + i * (2 * math.pi / 6)
                x = mouse_x + radius * math.cos(angle)
                y = mouse_y + radius * math.sin(angle)
                points.append((x, y))
            pygame.draw.polygon(screen, (0, 255, 0), points, 3)  # Green hexagon
        self.hexagon_repeat_draw -= 1

    def update_angle(self):
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0



