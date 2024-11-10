from rich.table import Table
from rich.console import Console
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url_template = "https://studies.cs.helsinki.fi/nhlstats/{}/players"
    console = Console()

    season = console.input("Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]: ")
    url = url_template.format(season)

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = console.input("Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR] (or press Enter to quit): ").upper()

        if not nationality:
            break
        players = stats.top_scorers_by_nationality(nationality)

        console.print(f"\nTop scorers of {nationality} season {season}\n", style="bold")
        table = Table(title="Player Stats")

        table.add_column("name", style="cyan", justify="left")
        table.add_column("team", style="magenta", justify="center")
        table.add_column("goals", style="green", justify="center")
        table.add_column("assists", style="blue", justify="center")
        table.add_column("points", style="yellow", justify="center")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        console.print(table)

if __name__ == "__main__":
    main()