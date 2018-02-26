import unittest
import p15board

class p15boardtest(unittest.TestCase):
    def setUp(self):
        self.board = p15board.Board(4)
        self.board.isdone()

    def test_board_size(self):
        self.assertEqual(self.board._Board__rows_size, 4)
        
    def test_empy_exists(self):        
        self.assertFalse(self.board.isdone(), "The board isn't null")



if __name__ == '__main__':
    unittest.main()