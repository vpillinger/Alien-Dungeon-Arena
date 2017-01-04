import unittest
import TurnTaker


class MyTestCase(unittest.TestCase):

    def test_move_when_no_enemies_in_sight(self):
        self.assertEqual(1, self.turn_taker.take_turn())

    def test_attack_when_enemies_are_in_sight(self):
        self.turn_taker.sight = MockSight
        self.assertEqual(10, self.turn_taker.take_turn())

    def setUp(self):
        self.turn_taker = TurnTaker.TurnTaker(MockBlankSight(), MockMove(), MockAttack())

class MockBlankSight():
    def enemies_in_sight(self):
        return {}

class MockSight():
    def enemies_in_sight(self):
        return {10}

class MockAttack():
    def attack(self, enemy):
        return enemy

class MockMove():
    def move(self):
        return 1

if __name__ == '__main__':
    unittest.main()
