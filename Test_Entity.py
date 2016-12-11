import unittest
import Entity

class Test_Entity(unittest.TestCase):

    def test_blocks_vision_property_is_set(self):
        self.assertEqual(True, self.entity.blocks_vision)
        entity = Entity.Entity(TurnTaker(), Hp_Manager(), False)
        self.assertEqual(False, entity.blocks_vision)

    def test_should_return_cd_in_aut_from_turn_taker(self):
        self.assertEqual(10, self.entity.take_turn())

    def test_should_pass_damage_type_and_damage_to_hp_manager(self):
        self.assertEqual(True, self.entity.get_hit("bullet", 10))

    def test_should_mark_self_for_destruction_when_Hp_Manager_get_hit_returns_true(self):
        self.entity.get_hit("bullet", 10)
        self.assertEqual(True, self.entity.marked_for_destruction)

    def test_should_not_mark_self_for_destruction_when_Hp_Manager_get_hit_returns_false(self):
        self.entity.get_hit("not-bullet", 5)
        self.assertEqual(False, self.entity.marked_for_destruction)

    def setUp(self):
        turn_taker = TurnTaker()
        hp_manager = Hp_Manager()
        self.entity = Entity.Entity(turn_taker, hp_manager)


class TurnTaker():
    def take_turn(self):
        return 10


class Hp_Manager():
    def get_hit(self, damage_type, damage):
        if(damage_type == "bullet" and damage == 10):
            return True
        return False

if __name__ == '__main__':
    unittest.main()
