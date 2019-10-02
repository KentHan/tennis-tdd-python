class TennisScore(object):
    def __init__(self, player_1_name, player_2_name):
        self.player_1_score = 0
        self.player_2_score = 0
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.score_mapping = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def get_score(self):
        if self.is_same_score():
            return self.get_deuce_status() if self.is_deuce() else self.get_tie_score()
        else:
            return self.get_status() if self.is_win_or_adv() else self.lookup_score()

    def get_deuce_status(self):
        return 'Deuce'

    def get_tie_score(self):
        return '%s All' % self.score_mapping[self.player_1_score]

    def lookup_score(self):
        return '%s %s' % (self.score_mapping[self.player_1_score]
                          , self.score_mapping[self.player_2_score])

    def get_status(self):
        return '%s %s' % (self.get_leader(), ('Win' if self.is_win() else 'Adv'))

    def get_adv_status(self):
        return '%s Adv' % self.get_leader()

    def get_leader(self):
        return self.player_1_name if self.player_1_score > self.player_2_score else self.player_2_name

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

    def is_adv(self):
        return self.player_1_score >= 3 and self.player_2_score >= 3 and abs(self.player_1_score - self.player_2_score) == 1

    def is_win(self):
        return (self.player_1_score >= 4 or self.player_2_score >= 4) and abs(self.player_1_score - self.player_2_score) >= 2

    def is_win_or_adv(self):
        return self.is_win() or self.is_adv()

    def is_same_score(self):
        return self.player_1_score == self.player_2_score

