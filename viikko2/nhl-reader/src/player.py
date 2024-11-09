class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.team = player_dict["team"]
        self.goals = player_dict["goals"]
        self.assists = player_dict["assists"]
        self.nationality = player_dict["nationality"]

    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
