ON_FIGHT_TEST_CASES = [
    {"test_input": {'HP': 30, 'profession': 'book', 'inventory': [], 'monster_counter': 0}, "expected": []},
    {"test_input": {'HP': 30, 'profession': 'book', 'inventory': [('sword', 5)], 'monster_counter': 0},
     "expected": [('sword', 5)]},
    {"test_input": {'HP': 30, 'profession': 'book', 'inventory': [('sword', 5), ('bow', 5)], 'monster_counter': 0},
     "expected": [('sword', 5)]},
    {"test_input": {'HP': 30, 'profession': 'book', 'inventory': [('sword', 5), ('bow', 5), ('arrows', 50)],
                    'monster_counter': 0}, "expected": [('sword', 5), ('bow', 5)]},
    {"test_input": {'HP': 30, 'profession': 'book', 'inventory': [('sword', 5), ('book', 5), ('arrows', 50)],
                    'monster_counter': 0}, "expected": [('sword', 5), ('book', 5)]},
    {"test_input": {'HP': 30, 'profession': 'book', 'inventory': [('sword', 5), ('book', 5), ('book', 5), ('book', 5)],
                    'monster_counter': 0}, "expected": [('sword', 5), ('book', 5), ('book', 5), ('book', 5)]},
    {"test_input": {'HP': 30, 'profession': 'book', 'inventory': [('totem',  {'HP': 30, 'profession': 'book',
                    'inventory': [], 'monster_counter': 0})],'monster_counter': 0}, "expected": []},
]

ENEMY_SPAWNER_TEST_CASES = [
    {"test_input": "HP", "expected": 1},
]
