
class SpellCaster:
    def __init__(self, screen, spell_list):
        self.screen = screen
        self.spell_list = spell_list
        self.targets_to_click = set()

    def updateInfo(self, mouse_pos, target_list):
        self.mouse_pos = mouse_pos
        self.target_list = target_list
        
    def cast_spell(self, spell_position):
        spell = self.spell_list[spell_position][0]
        return spell.cast(self.screen, self.mouse_pos, self.target_list)
    
    def check_spell_list(self):
        for i, spell_info in enumerate(self.spell_list):
            if spell_info[1] > 0:
                self.targets_to_click.update(self.cast_spell(i, self.mouse_pos, self.target_list)) 
                spell_info[1] -= 1

        return list(self.targets_to_click)
