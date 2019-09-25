import unittest

from tennis_score import TennisScore


class TennisScoreTest(unittest.TestCase):

   def test_love_all(self):
       sut = TennisScore()
       self.assertEqual("Love All", sut.getScore())
