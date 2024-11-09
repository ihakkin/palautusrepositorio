import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = [Player(player_dict) for player_dict in response]

    finnish_players = sorted(
        (player for player in players if player.nationality == "FIN"),
        key=lambda player: player.points,
        reverse=True
    )

    print("Players from FIN\n")
    for player in finnish_players:
        print(player)


if __name__ == "__main__":
    main()