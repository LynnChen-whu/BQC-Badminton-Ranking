# -*- coding = utf-8 -*-
# @Time : 2021-4-2 8:21
# @Author : Lynn
# @File : Elo_Module.py
# @Software : PyCharm

class Player(object):
    def __init__(self, name: str, rating: int = 1370):
        self.name = name
        self.rating = rating

    def get_name(self) -> str:
        return self.name

    def get_rating(self) -> int:
        return self.rating

    def change_name(self, name: str):
        self.name = name

    def change_rating(self, rating: int = 1370):
        self.rating = rating


class Ranking_System(object):
    def __init__(self, name: str = 'Rankings_System', player_list: list[Player] = []):
        self.name = name
        self.player_list = player_list
        self.rankings = {}
        self.rank()

    def add_player(self, player: Player):
        self.player_list.append(player)

    def remove_player(self, player: Player):
        for index in range(len(self.player_list)):
            if self.player_list[index] == player:
                del self.player_list[index]
        self.rank()

    @staticmethod
    def get_player_s_rating(player: Player) -> int:
        return player.get_rating()

    def rank(self):
        self.rankings.clear()
        self.player_list.sort(key=self.get_player_s_rating, reverse=True)
        for index in range(len(self.player_list)):
            self.rankings[index + 1] = self.player_list[index]

    def get_rankings(self):
        return self.rankings

    def inquire_by_ranking(self, ranking: int = 1) -> tuple[str, int] or str:
        if ranking in self.rankings:
            return self.rankings[ranking].get_name(), self.rankings[ranking].get_rating()
        else:
            return '该排名不存在'

    def inquire_by_name(self, name: str = '') -> tuple[int, int] or str:
        for ranking in list(self.rankings.keys()):
            if self.rankings[ranking].get_name() == name:
                break
        else:
            return '没有找到该选手'
        return ranking, self.rankings[ranking].get_rating()

    @staticmethod
    def elo_win_rate_predict(player1: Player,
                             team: list[Player] = [], opponents: list[Player] = []) -> float or str:
        if team == [] or opponents == []:
            return ValueError
        teammates_rating = 0
        opponents_rating = 0
        for teammate in team:
            teammates_rating += teammate.get_rating()
        for opponent in opponents:
            opponents_rating += opponent.get_rating()
        difference = player1.get_rating() - player1.get_rating() * opponents_rating / teammates_rating
        return 1 / (1 + 10 ** (- difference / 400))

    @staticmethod
    def elo_rating_calculate(player: Player, win_rate_prediction: float,
                             result: float, K:float = 17) -> int:
        return int(round(player.get_rating() + K * (result - win_rate_prediction)))

    def match(self, team0: list[Player] = [], team1: list[Player] = [], result: float = 0, K: float = 17):
        if team0 == [] or team1 == []:
            return ValueError
        win_rate_prediction_list_0 = []
        win_rate_prediction_list_1 = []
        for player in team0:
            win_rate_prediction_list_0.append(self.elo_win_rate_predict(player, team0, team1))
        for player in team1:
            win_rate_prediction_list_1.append(self.elo_win_rate_predict(player, team1, team0))
        for index in range(len(team0)):
            new_rating = self.elo_rating_calculate(team0[index], win_rate_prediction_list_0[index], result, K)
            team0[index].change_rating(new_rating)
        for index in range(len(team1)):
            new_rating = self.elo_rating_calculate(team1[index], win_rate_prediction_list_1[index], result, K)
            team1[index].change_rating(new_rating)
