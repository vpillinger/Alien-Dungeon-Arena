class Entity():
    """
    A class that represents physical entities (players, items, enemies, terrain objects).
    The purpose of this class to to provide a common interface for properties that all
    physical objects have.
    """

    def __init__(self, turn_taker, hp_manager, blocks_vision = True):
        self.turn_taker = turn_taker
        self.hp_manager = hp_manager
        self.marked_for_destruction = False
        self.blocks_vision = blocks_vision

    def take_turn(self):
        """ Use this entity's TurnTaker to take a game turn. It returns an integer cd value in AUT."""
        return self.turn_taker.take_turn()

    def get_hit(self, damage_type, damage):
        """ Use this entity's HPManager to take damage (and possibly get destroyed)."""
        is_destroyed = self.hp_manager.get_hit(damage_type, damage)
        if (is_destroyed):
            self.mark_for_destruction()
        return is_destroyed

    def blocks_vision(self):
        """Return whether this entity blocks vision (whether other entities can see past it)."""
        return self.blocks_vision

    def mark_for_destruction(self):
        """Mark this entity for destruction."""
        self.marked_for_destruction = True

    def unmark_for_destruction(self):
        """Unmark this entity for destruction."""
        self.marked_for_destruction = False