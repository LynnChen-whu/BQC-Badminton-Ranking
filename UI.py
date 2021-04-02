# -*- coding = utf-8 -*-
# @Time : 2021-4-2 14:29
# @Author : Lynn
# @File : UI.py
# @Software : PyCharm

import time
import Elo_Module
import txt_r_w
import easygui

def list_is_dig_list(list_in: list[str]) -> bool:
    for str_in in list_in:
        if not str_in.isdigit():
            return False
    return True

def list_is_key_list(list_in: list, dic_in: dict) -> bool:
    for key in list_in:
        if not key in list(dic_in.keys()):
            return False
    return True


if __name__ == '__main__':
    start = time.process_time()


    if easygui.ccbox('请选择你要打开的排名系统', '选择', ['单打', '双打']):
        player_data_list = txt_r_w.read_lines_from_txt('Singles')
        name = '单打排名'
    else:
        player_data_list = txt_r_w.read_lines_from_txt('Doubles')
        name = '双打排名'


    '''初始化'''
    player_list = []
    for item in player_data_list:
        player_data_temp = item.split('：')  # 每行为一个选手的数据，数据格式是“名字：等级分”，冒号是中文字符
        player_list.append(Elo_Module.Player(player_data_temp[0], int(player_data_temp[1])))
    ranking_system = Elo_Module.Ranking_System(name, player_list)


    while 1:

        print(f'当前{name}情况如下')
        ranking_list = list(ranking_system.get_rankings().keys())
        ranking_list.sort()
        for ranking in ranking_list:
            print(str(ranking).rjust(3) + '\t' + ranking_system.get_rankings()[ranking].get_name().ljust(7) +
                  '\t' + str(ranking_system.get_rankings()[ranking].get_rating()).rjust(5))


        flag = easygui.buttonbox('请选择你要进行的操作', name, ['录入比赛结果', '新增选手', '退出系统'])

        if flag == '录入比赛结果':

            team1 = easygui.enterbox('请输入胜方当前的排名，不同选手间用小数点“.”隔开', flag, ).split('.')
            while not list_is_dig_list(team1):
                team1 = easygui.enterbox('输入非法，请重新输入胜方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
            for index in range(len(team1)):
                team1[index] = int(team1[index])
            while not list_is_key_list(team1, ranking_system.get_rankings()):
                team1 = easygui.enterbox('输入非法，请重新输入胜方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
            team1 = ranking_system.get_player_list_by_ranking_list(team1)

            team0 = easygui.enterbox('请输入败方当前的排名，不同选手间用小数点“.”隔开', flag, ).split('.')
            while len(team0) != len(team1):
                team0 = easygui.enterbox('输入非法，请重新输入败方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
            while not list_is_dig_list(team0):
                team0 = easygui.enterbox('输入非法，请重新输入败方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
            for index in range(len(team0)):
                team0[index] = int(team0[index])
            while not list_is_key_list(team0, ranking_system.get_rankings()):
                team0 = easygui.enterbox('输入非法，请重新输入败方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
            team0 = ranking_system.get_player_list_by_ranking_list(team0)

            ranking_system.match(team0, team1, 0, 17)


        elif flag == '新增选手':


        elif flag == '退出系统':


    end = time.process_time()
    print(f'runtime = {end - start}')
