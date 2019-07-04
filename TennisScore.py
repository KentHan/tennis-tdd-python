class TennisScore(object):

    def __init__(self):
        self.first_player_score = 0

    def first_player_scored(self):
        self.first_player_score +=1

    def score(self):
        if self.first_player_score is 1:
            return "Fifteen Love"
        if self.first_player_score is 2:
            return "Thirty Love"
        return "Love All"

