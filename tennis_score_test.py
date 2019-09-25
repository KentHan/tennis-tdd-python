import unittest

from tennis_score import TennisScore


class TennisScoreTest(unittest.TestCase):

   def test_love_all(self):
       sut = TennisScore()
       self.assertEqual("Love All", sut.get_score())

   def test_fifteen_love(self):
       sut = TennisScore()
       sut.add_score(1,1)
       self.assertEqual("Fifteen Love", sut.get_score())

   def test_thirty_love(self):
       sut = TennisScore()
       sut.add_score(1,2)
       self.assertEqual("Thirty Love", sut.get_score())

   def test_forty_love(self):
       sut = TennisScore()
       sut.add_score(1, 3)
       self.assertEqual("Forty Love", sut.get_score())

   def test_love_fifteen(self):
       sut = TennisScore()
       sut.add_score(2, 1)
       self.assertEqual("Love Fifteen", sut.get_score())

   def test_love_thirty(self):
       sut = TennisScore()
       sut.add_score(2, 2)
       self.assertEqual("Love Thirty", sut.get_score())

   def test_love_forty(self):
       sut = TennisScore()
       sut.add_score(2, 3)
       self.assertEqual("Love Forty", sut.get_score())

   def test_fifteen_all(self):
       sut = TennisScore()
       sut.add_score(1, 1)
       sut.add_score(2, 1)
       self.assertEqual("Fifteen All", sut.get_score())