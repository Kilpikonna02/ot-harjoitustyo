import unittest
from level import Level

LEVEL_MAP = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,3,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

CELL_SIZE = 50

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP, CELL_SIZE)
    
    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x,x)
        self.assertEqual(sprite.rect.y,y)
    
    def test_can_move_in_floor(self):
        snake = self.level.snake

        self.assert_coordinates_equal(snake, 8 * CELL_SIZE, 9 * CELL_SIZE)

        self.level.move_snake(dy=-CELL_SIZE)
        self.assert_coordinates_equal(snake, 8 * CELL_SIZE, 8 * CELL_SIZE)

        self.level.move_snake(dx=-CELL_SIZE)
        self.assert_coordinates_equal(snake, 7 * CELL_SIZE, 8 * CELL_SIZE)