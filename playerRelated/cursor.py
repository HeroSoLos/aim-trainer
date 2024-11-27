import random
import math

class Cursor:
    def __init__(self, position, health, mana, spell_list=None, passive_buffs=None) -> None:
        if spell_list is None:
            spell_list = []
        if passive_buffs is None:
            passive_buffs = []
        self.position = position
        self.health = health
        self.mana = mana
        self.spell_list = spell_list
        self.passive_buffs = passive_buffs
    def cast_spell(self, spell):
        pass