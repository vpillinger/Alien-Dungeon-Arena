import unittest
import HpManager

class Test_HpManager(unittest.TestCase):

    def test_should_heal_full_amount_if_final_amount_is_less_than_max(self):
        self.hp_manager.heal(50)
        self.assertEqual(75, self.hp_manager.current_hp)

    def test_should_cap_healing_at_max_hp(self):
        self.hp_manager.heal(100)
        self.assertEqual(100, self.hp_manager.current_hp)

    def test_take_damage_should_reduce_current_hp_by_specified_amount(self):
        self.hp_manager.take_damage("normal", 15)
        self.assertEqual(10, self.hp_manager.current_hp)

    def test_take_damage_should_return_false_if_final_hp_greater_than_0(self):
        self.assertEqual(False, self.hp_manager.take_damage("normal", 15))

    def test_take_damage_should_return_true_if_final_hp_less_than_0(self):
        self.assertEqual(True, self.hp_manager.take_damage("normal", 150))

    def test_take_damage_should_return_true_if_final_hp_equal_to_0(self):
        self.assertEqual(True, self.hp_manager.take_damage("normal", 25))

    def setUp(self):
        self.hp_manager = HpManager.Hp_Manager(100)
        self.hp_manager.current_hp = 25

if __name__ == '__main__':
    unittest.main()
