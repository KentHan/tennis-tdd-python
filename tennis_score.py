class TennisScore(object):
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0

    def get_score(self):
        if self.player_1_score + self.player_2_score == 0:
            return "Love All"
        elif self.player_1_score == 1 and self.player_2_score == 0:
            return "Fifteen Love"
        elif self.player_1_score == 2 and self.player_2_score == 0:
            return "Thirty Love"
        elif self.player_1_score == 3 and self.player_2_score == 0:
            return "Forty Love"

    def add_score(self, player, times):
        if player == 1:
            self.player_1_score += times
        elif player == 2:
            self.player_2_score += times
        else:
            raise Exception("only two player")