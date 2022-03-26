import unittest
from tests.constant_test_cases import ON_FIGHT_TEST_CASES, ENEMY_SPAWNER_TEST_CASES
from main import apple, on_fight, enemy_spawner
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class SomeTestCase(unittest.TestCase):
    """Такие же тестовые случаи, но реализованные через unittest."""

    def test_apple(self):
        """Тесирование яблока."""
        self.assertGreaterEqual(6, apple())
        self.assertLessEqual(2, apple())


    def test_on_fight(self):
        """Тесирование on_fight."""
        for test_case in ON_FIGHT_TEST_CASES:
            test_inp = test_case.get("test_input")
            expected = test_case.get("expected")
            self.assertEqual(expected, on_fight(test_inp))


    def test_mass_choice(self):
        """Тесирование mass_choice."""
        for test_case in ENEMY_SPAWNER_TEST_CASES:
            test_inp = test_case.get("test_input")
            expected = test_case.get("expected")
            self.assertLessEqual(expected, enemy_spawner()[test_inp])