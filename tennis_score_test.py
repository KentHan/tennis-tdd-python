import unittest

from tennis_score import TennisScore


class TennisScoreTest(unittest.TestCase):
    def setUp(self):
        self.sut = TennisScore('Ace', 'Ben')

    def test_love_all(self):
        self.assertEqual("Love All", self.sut.get_score())

    def test_fifteen_love(self):
        self.sut.add_score(1, 1)
        self.assertEqual("Fifteen Love", self.sut.get_score())

    def test_thirty_love(self):
        self.sut.add_score(1, 2)
        self.assertEqual("Thirty Love", self.sut.get_score())

    def test_forty_love(self):
        self.sut.add_score(1, 3)
        self.assertEqual("Forty Love", self.sut.get_score())

    def test_love_fifteen(self):
        self.sut.add_score(2, 1)
        self.assertEqual("Love Fifteen", self.sut.get_score())

    def test_love_thirty(self):
        self.sut.add_score(2, 2)
        self.assertEqual("Love Thirty", self.sut.get_score())

    def test_love_forty(self):
        self.sut.add_score(2, 3)
        self.assertEqual("Love Forty", self.sut.get_score())

    def test_fifteen_all(self):
        self.sut.add_score(1, 1)
        self.sut.add_score(2, 1)
        self.assertEqual("Fifteen All", self.sut.get_score())

    def test_thirty_all(self):
        self.sut.add_score(1, 2)
        self.sut.add_score(2, 2)
        self.assertEqual("Thirty All", self.sut.get_score())


    def test_deuce(self):
        self.sut.add_score(1, 3)
        self.sut.add_score(2, 3)
        self.assertEqual("Deuce", self.sut.get_score())

    def test_Ace_adv(self):
        self.sut.add_score(1, 4)
        self.sut.add_score(2, 3)
        self.assertEqual("Ace Adv", self.sut.get_score())

    def test_Ben_adv(self):
        self.sut.add_score(1, 3)
        self.sut.add_score(2, 4)
        self.assertEqual("Ben Adv", self.sut.get_score())

    def test_Ace_win(self):
        self.sut.add_score(1, 5)
        self.sut.add_score(2, 3)
        self.assertEqual("Ace Win", self.sut.get_score())

    def test_Ben_win(self):
        self.sut.add_score(1, 3)
        self.sut.add_score(2, 5)
        self.assertEqual("Ben Win", self.sut.get_score())

    def test_4_1(self):
        self.sut.add_score(1, 4)
        self.sut.add_score(2, 1)
        self.assertEqual("Ace Win", self.sut.get_score())

    def test_1_4(self):
        self.sut.add_score(1, 1)
        self.sut.add_score(2, 4)
        self.assertEqual("Ben Win", self.sut.get_score())
