class TennisScore(object):
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.score_mapping = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def get_score(self):
        if self.player_1_score == self.player_2_score:
            return '%s All' % self.score_mapping[self.player_1_score]
        else:
            return '%s %s' % (self.score_mapping[self.player_1_score]
                              , self.score_mapping[self.player_2_score])

    def add_score(self, player, times):
        if player == 1:
            self.player_1_score += times
        elif player == 2:
            self.player_2_score += times
        else:
            raise Exception("only two player")
