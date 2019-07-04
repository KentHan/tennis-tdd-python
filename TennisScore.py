class TennisScore(object):

    def __init__(self):
        self.score_map = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.second_player_score = 0
        self.first_player_score = 0

    def first_player_scored(self):
        self.first_player_score += 1

    def second_player_scored(self):
        self.second_player_score += 1

    def score(self):
        if self.first_player_score is self.second_player_score:
            return f"{self.score_map[self.first_player_score]} All"
        if self.second_player_score > 0:
            return f"Love {self.score_map[self.second_player_score]}"
        if self.first_player_score > 0:
            return f"{self.score_map[self.first_player_score]} Love"
