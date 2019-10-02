class TennisScore(object):
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.score_mapping = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def get_score(self):
        if self.player_1_score == self.player_2_score:
            if self.player_1_score >= 3:
                return 'Deuce'
            return '%s All' % self.score_mapping[self.player_1_score]

        else:
            if self.player_1_score >= 3 and self.player_1_score - self.player_2_score == 1:
                return 'Ace Adv'
            return '%s %s' % (self.score_mapping[self.player_1_score]
                              , self.score_mapping[self.player_2_score])

    def add_score(self, player, times):
        if player == 1:
            self.player_1_score += times
        elif player == 2:
            self.player_2_score += times
        else:
            raise Exception("only two player")
