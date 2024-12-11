
class SpellCaster:
    def __init__(self, spell_list):
        self.spell_list = spell_list
        self.targets_to_click = set()

    def cast_spell(self, screen, spell_position, mouse_pos, target_list):
        spell = self.spell_list[spell_position][0]
        return spell.cast(screen, mouse_pos, target_list)

    def check_spell_list(self, screen, mouse_pos, target_list):
        for i, spell_info in enumerate(self.spell_list):
            if spell_info[1] > 0:
                self.targets_to_click.update(self.cast_spell(screen, i, mouse_pos, target_list)) #TODO: currently returns a list which cannot be added to a set, need to change it into individual items!!!
                spell_info[1] -= 1

        return list(self.targets_to_click)
