import random
import math

class Cursor:
    def __init__(self, position, health, mana, spell_list=[], passive_buffs=[]) -> None:
        self.position = position
        self.health = health
        self.mana = mana
        self.spell_list = spell_list
        self.passive_buffs = passive_buffs
    def cast_spell(self, spell):
        pass