import unittest

from TennisScore import TennisScore


class TennisScoreTest(unittest.TestCase):

    def setUp(self):
        self.sut = TennisScore(f"Ace", f"Pro")

    def test_love_all(self):
        self.assertEqual("Love All", self.sut.score())

    def test_fifteen_love(self):
        self.first_player_scored(1)
        self.assertEqual("Fifteen Love", self.sut.score())

    def test_thirty_love(self):
        self.first_player_scored(2)
        self.assertEqual("Thirty Love", self.sut.score())

    def test_forty_love(self):
        self.first_player_scored(3)
        self.assertEqual("Forty Love", self.sut.score())

    def test_love_fifteen(self):
        self.second_player_scored(1)
        self.assertEqual("Love Fifteen", self.sut.score())

    def test_fifteen_all(self):
        self.first_player_scored(1)
        self.second_player_scored(1)
        self.assertEqual("Fifteen All", self.sut.score())

    def test_deuce(self):
        self.deuce()
        self.assertEqual("Deuce", self.sut.score())

    def test_first_player_adv(self):
        self.deuce()
        self.first_player_scored(1)
        self.assertEqual("Ace adv", self.sut.score())

    def test_first_player_win(self):
        self.deuce()
        self.first_player_scored(2)
        self.assertEqual("Ace win", self.sut.score())

    def test_second_player_win(self):
        self.first_player_scored(2)
        self.second_player_scored(4)
        self.assertEqual("Pro win", self.sut.score())

    def deuce(self):
        self.first_player_scored(3)
        self.second_player_scored(3)

    def first_player_scored(self, times):
        for i in range(times):
            self.sut.first_player_scored()

    def second_player_scored(self, times):
        for i in range(times):
            self.sut.second_player_scored()


if __name__ == '__main__':
    unittest.main()
