import unittest

from tennis_score import TennisScore


class TennisScoreTest(unittest.TestCase):

   def test_love_all(self):
       sut = TennisScore()
       self.assertEqual("Love All", sut.get_score())

   def test_fiften_love(self):
       sut = TennisScore()
       sut.add_score(1,1)
       self.assertEqual("Fifteen Love", sut.get_score())

   def test_thirty_love(self):
       sut = TennisScore()
       sut.add_score(1,2)
       self.assertEqual("Thirty Love", sut.get_score())