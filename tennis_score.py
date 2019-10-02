class TennisScore(object):
    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.score_mapping = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def get_score(self):
        if self.player_1_score == self.player_2_score:
            if self.is_deuce():
                return 'Deuce'
            return '%s All' % self.score_mapping[self.player_1_score]

        else:
            if self.is_Adv():
                if self.player_1_score > self.player_2_score:
                    return 'Ace Adv'
                else:
                    return 'Ben Adv'
            elif self.player_1_score >= 4 and self.player_1_score - self.player_2_score >= 2:
                return 'Ace Win'
            elif self.player_2_score >= 4 and self.player_2_score - self.player_1_score >= 2:
                return 'Ben Win'
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

    def is_deuce(self):
        if self.player_1_score == self.player_2_score and self.player_2_score >= 3:
            return True
        else:
            return False

    def is_Adv(self):
        return self.player_1_score >= 3 and self.player_2_score >= 3 and abs(self.player_1_score - self.player_2_score) == 1
