class TennisScore(object):

    def __init__(self, first_player_name, second_player_name):
        self.score_map = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.second_player_score = 0
        self.first_player_score = 0
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name

    def first_player_scored(self):
        self.first_player_score += 1

    def second_player_scored(self):
        self.second_player_score += 1

    def score(self):
        return (self.deuce() if self.is_deuce() else self.same_score()) if self.is_same_score() else (
            self.adv_score() if self.is_adv_state() else self.look_up_score())

    def look_up_score(self):
        return f"{self.score_map[self.first_player_score]} {self.score_map[self.second_player_score]}"

    def adv_score(self):
        return f"{self.winner()} adv" if self.game_point() else f"{self.winner()} win"

    def same_score(self):
        return f"{self.score_map[self.first_player_score]} All"

    def deuce(self):
        return f"Deuce"

    def game_point(self):
        return abs(self.first_player_score - self.second_player_score) == 1

    def winner(self):
        return self.first_player_name if self.first_player_score > self.second_player_score else self.second_player_name

    def is_same_score(self):
        return self.first_player_score is self.second_player_score

    def is_deuce(self):
        return self.first_player_score >= 3

    def is_adv_state(self):
        return self.first_player_score > 3 or self.second_player_score > 3
