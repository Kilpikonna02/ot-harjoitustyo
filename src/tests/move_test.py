import unittest
from gameloop import GameLoop


class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.snakeposx = 0
        self.snakeposy = 0
    
    def assert_coordinates_equal(self, snakeposx,x,snakeposy,y):
        self.assertEqual(snakeposx,x)
        self.assertEqual(snakeposy,y)

    def move(self,snake_speed_x,snake_speed_y):
        self.snakeposx += snake_speed_x
        self.snakeposy += snake_speed_y
    
    def test_can_move(self):

        self.assert_coordinates_equal(self.snakeposx,0,self.snakeposy,0)
        self.move(20,0)
        self.assert_coordinates_equal(self.snakeposx,20,self.snakeposy,0)
        self.move(0,100)
        self.assert_coordinates_equal(self.snakeposx,20,self.snakeposy,100)