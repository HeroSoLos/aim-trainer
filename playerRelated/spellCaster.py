
class SpellCaster:
    def __init__(self, spell_list):
        self.spell_list = spell_list

        self.targets_to_click = {}

    def cast_spell(self, spell_position, mouse_pos, target_list):
        spell = self.spell_list[spell_position]
        return spell.cast(mouse_pos, target_list)

    def check_spell_list(self, mouse_pos, target_list):
        for i, spell_info in enumerate(self.spell_list):
            if spell_info[1] > 0:
                self.cast_spell(i, mouse_pos, target_list)
                spell_info[1] -= 1 #TODO: make target hashable so i can add to a set