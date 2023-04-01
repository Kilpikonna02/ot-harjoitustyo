import unittest
from death import Death


class TestDeath(unittest.TestCase):
    def setUp(self):
        self.death = Death()
        self.snakeposx = 300
        self.snakeposy = 300
    
    def assert_coordinates_equal(self, snakeposx,snakeposy, true_or_false):
        self.assertEqual(self.death.check_death(snakeposx,snakeposy),true_or_false)

    def move(self,snake_speed_x,snake_speed_y):
        self.snakeposx += snake_speed_x
        self.snakeposy += snake_speed_y
    
    def test_can_die(self):
        self.assert_coordinates_equal(self.snakeposx,self.snakeposy, False)
        self.move(600,0)
        self.assert_coordinates_equal(self.snakeposx,self.snakeposy, True)