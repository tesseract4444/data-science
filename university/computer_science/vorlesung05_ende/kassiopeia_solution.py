from unittest import TestCase
from typing import List, Tuple


def get_neighbors(x: int, y: int, field_max_x: int, field_max_y: int) -> List[Tuple[int, int]]:
    neighbors: List[Tuple[int, int]] = []

    if y > 0:  # can go left
        neighbors.append((x, y - 1))

    if y < field_max_y - 1:  # can go right
        neighbors.append((x, y + 1))

    if x > 0:  # can go down
        neighbors.append((x - 1, y))

    if x < field_max_x - 1:  # can go up
        neighbors.append((x + 1, y))

    return neighbors


def test_survivable(start: Tuple[int, int], field: List[List[str]]) -> bool:
    neighbors: List[Tuple[int, int]] = [start]

    while len(neighbors) != 0:

        # Using tuple unpacking
        actual_x, actual_y = neighbors.pop(0)
        field[actual_x][actual_y] = 'V'
        new_neighbors = get_neighbors(actual_x, actual_y, len(field), len(field[0]))

        for coord in new_neighbors:
            if field[coord[0]][coord[1]] == '_':
                neighbors.append(coord)

    for row in field:
        for cell in row:
            if cell == '_':
                return False

    return True


class KassiopeiaTest(TestCase):
    not_possible_field: List[List[str]] = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', '_', '_', 'X', '_', '_', '_', '_', 'X'],
        ['X', '_', '_', 'X', '_', '_', '_', '_', 'X'],
        ['X', '_', '_', '_', '_', 'X', 'X', 'X', 'X'],
        ['X', '_', '_', '_', '_', 'X', '_', '_', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ]

    possible_field: List[List[str]] = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', '_', '_', 'X', '_', '_', '_', '_', 'X'],
        ['X', '_', '_', 'X', '_', '_', '_', '_', 'X'],
        ['X', '_', '_', '_', '_', 'X', '_', '_', 'X'],
        ['X', '_', '_', '_', '_', 'X', '_', '_', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ]

    def test_get_neighbors(self):
        # Using set so order is not considered
        self.assertEqual({(1, 0), (0, 1)}, set(get_neighbors(0, 0, 5, 5)))
        self.assertEqual({(3, 0), (4, 1)}, set(get_neighbors(4, 0, 5, 5)))
        self.assertEqual({(0, 3), (1, 4)}, set(get_neighbors(0, 4, 5, 5)))
        self.assertEqual({(3, 4), (4, 3)}, set(get_neighbors(4, 4, 5, 5)))
        self.assertEqual({(0, 1), (1, 2), (2, 1), (1, 0)}, set(get_neighbors(1, 1, 5, 5)))

    def test_kassiopeia(self):
        self.assertTrue(test_survivable((1, 1), self.possible_field))

        self.assertFalse(test_survivable((1, 1), self.not_possible_field))

        self.assertFalse(test_survivable((0, 0), [
            ['_', '_', '_'],
            ['X', 'X', 'X'],
            ['_', '_', '_']
        ]))
        self.assertFalse(test_survivable((2, 2), [
            ['_', '_', '_'],
            ['X', 'X', 'X'],
            ['_', '_', '_']
        ]))
