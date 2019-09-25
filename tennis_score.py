class TennisScore(object):
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0

    def get_score(self):
        if self.player_1_score + self.player_2_score == 0:
            return "Love All"
        elif self.player_1_score == 1 and self.player_2_score == 0:
            return "Fifteen Love"

    def add_score(self, player):
        if player == 1:
            self.player_1_score += 1
        elif player == 2:
            self.player_2_score += 1
        else:
            raise Exception("only two player")