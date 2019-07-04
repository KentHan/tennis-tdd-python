import unittest

from TennisScore import TennisScore


class TennisScoreTest(unittest.TestCase):

    def setUp(self):
        self.sut = TennisScore()

    def test_love_all(self):
        self.assertEqual("Love All", self.sut.score())

    def test_fifteen_love(self):
        self.first_player_scored(1)
        self.assertEqual("Fifteen Love", self.sut.score())

    def test_thirty_love(self):
        self.first_player_scored(2)
        self.assertEqual("Thirty Love", self.sut.score())

    def first_player_scored(self, times):
        for i in range(times):
            self.sut.first_player_scored()


if __name__ == '__main__':
    unittest.main()