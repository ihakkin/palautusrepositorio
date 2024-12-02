POINTS = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
class TennisGame:
    POINTS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_tie():
            return self.get_tie_score()
        elif self.is_endgame():
            return self.get_endgame_score()
        return self.get_running_score()

    def is_tie(self):
        return self.player1_score == self.player2_score

    def is_endgame(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def get_tie_score(self):
        if self.player1_score >= 3:
            return "Deuce"
        return f"{self.POINTS[self.player1_score]}-All"

    def get_endgame_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def get_running_score(self):
        return f"{self.POINTS[self.player1_score]}-{self.POINTS[self.player2_score]}"