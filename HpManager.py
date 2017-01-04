

class HpManager():
    """A class that manages hp for most entity types. (Future consideration armor types)"""

    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp

    def heal(self, amount):
        """ Heal the specified amount, capping at max_hp."""
        self.current_hp =  min(self.max_hp, self.current_hp + amount)

    def take_damage(self, damage_type, damage):
        """ Take the specified amount of damage (possibly modified by damage_type).
        Note: will heal (over max hp) if given a negative damage amount.
        Returns true if the entity should be destroyed by the damage taken"""
        self.current_hp -= damage
        return self.current_hp <= 0