# -*- coding = utf-8 -*-
# @Time : 2021/4/1 22:30
# @Author : Lynn
# @File : Elo_Module.py
# @Software : PyCharm

class Player(object):
    def __init__(self, name: str, rating: int = 137):
        self.name = name
        self.rating = rating

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def change_name(self, name: str):
        self.name = name

    def change_rating(self, rating: int = 137):
        self.rating = rating


class Ranking_System(object):
    def __init__(self, name: str = 'Ranking_System'):
        self.name = name
        self.player_list = []
        self.ranking = {}

    def add_player(self, player: Player):
        self.player_list.append(player)

    @staticmethod
    def get_player_s_rating(player: Player):
        return player.get_rating()

    def rank(self):
        self.player_list.sort(key=self.get_player_s_rating(), reverse=True)
        for index in range(len(self.player_list)):
            self.ranking[index + 1] = f'{self.player_list[index].get_name()}   {self.player_list[index].get_rating()}'