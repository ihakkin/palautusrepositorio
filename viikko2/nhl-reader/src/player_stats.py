from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [player for player in self.players if player.nationality == nationality]
        return sorted(filtered_players, key=lambda player: player.points, reverse=True)
