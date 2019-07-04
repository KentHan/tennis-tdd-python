import unittest

from TennisScore import TennisScore


class TennisScoreTest(unittest.TestCase):

    def test_love_all(self):
        sut = TennisScore()
        self.assertEqual("Love All", sut.score())

if __name__ == '__main__':
    unittest.main()