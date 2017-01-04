import random


class TurnTaker():
    """ This class contains the algorithm and necessary components to take a basic turn."""

    def __init__(self, sight, move, attack):
        self.sight = sight
        self.move = move
        self.attack = attack

    def take_turn(self):
        """Take a turn. If an enemy is in sight, shoot it, else move"""

        enemies_in_sight = self.sight.enemies_in_sight()
        if not enemies_in_sight:
            return self.move.move()
        return self.attack.attack(random.choice(enemies_in_sight))

