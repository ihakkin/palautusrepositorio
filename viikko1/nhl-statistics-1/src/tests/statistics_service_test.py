import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
        
    def test_search_nonexistent_player(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertEqual([player.name for player in edm_players], ["Semenko", "Kurri", "Gretzky"])

    def test_top(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3) 
        self.assertEqual([player.name for player in top_players], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_goals(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(len(top_players), 3) 
        self.assertEqual([player.name for player in top_players], ["Lemieux", "Yzerman", "Kurri"])

    def test_top_assists(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3) 
        self.assertEqual([player.name for player in top_players], ["Gretzky", "Yzerman", "Lemieux"])