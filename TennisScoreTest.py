import unittest

from TennisScore import TennisScore


class TennisScoreTest(unittest.TestCase):

    def setUp(self):
        self.sut = TennisScore(f"Ace", f"Pro")

    def test_love_all(self):
        self.score_should_be("Love All")

    def score_should_be(self, score):
        self.assertEqual(score, self.sut.score())

    def test_fifteen_love(self):
        self.first_player_scored(1)
        self.score_should_be("Fifteen Love")

    def test_thirty_love(self):
        self.first_player_scored(2)
        self.score_should_be("Thirty Love")

    def test_forty_love(self):
        self.first_player_scored(3)
        self.score_should_be("Forty Love")

    def test_love_fifteen(self):
        self.second_player_scored(1)
        self.score_should_be("Love Fifteen")

    def test_fifteen_all(self):
        self.first_player_scored(1)
        self.second_player_scored(1)
        self.score_should_be("Fifteen All")

    def test_deuce(self):
        self.deuce()
        self.score_should_be("Deuce")

    def test_first_player_adv(self):
        self.deuce()
        self.first_player_scored(1)
        self.score_should_be("Ace adv")

    def test_first_player_win(self):
        self.deuce()
        self.first_player_scored(2)
        self.score_should_be("Ace win")

    def test_second_player_win(self):
        self.first_player_scored(2)
        self.second_player_scored(4)
        self.score_should_be("Pro win")

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
