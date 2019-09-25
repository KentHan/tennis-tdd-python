class TennisScore(object):
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.score_mapping = {1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def get_score(self):
        if self.player_1_score + self.player_2_score == 0:
            return "Love All"
        elif self.player_2_score == 0:
            return '%s Love' % self.score_mapping[self.player_1_score]
        elif self.player_1_score == 0:
            return 'Love %s' % self.score_mapping[self.player_2_score]
        elif self.player_1_score == 1 and self.player_2_score == 1:
            return "Fifteen All"

    def add_score(self, player, times):
        if player == 1:
            self.player_1_score += times
        elif player == 2:
            self.player_2_score += times
        else:
            raise Exception("only two player")