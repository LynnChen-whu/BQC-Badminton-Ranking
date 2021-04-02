# -*- coding = utf-8 -*-
# @Time : 2021/4/2 22:24
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
        system_name = '单打排名'
    else:
        player_data_list = txt_r_w.read_lines_from_txt('Doubles')
        system_name = '双打排名'

    '''初始化'''
    player_list = []
    for item in player_data_list:
        if item == '':
            continue
        player_data_temp = item.split('：')  # 每行为一个选手的数据，数据格式是“名字：等级分”，冒号是中文字符
        player_list.append(Elo_Module.Player(player_data_temp[0], int(player_data_temp[1])))
    ranking_system = Elo_Module.Ranking_System(system_name, player_list)

    while 1:

        print(f'当前{system_name}情况如下')
        ranking_list = list(ranking_system.get_rankings().keys())
        ranking_list.sort()
        for ranking in ranking_list:
            print(str(ranking).rjust(3) + '\t' + ranking_system.get_rankings()[ranking].get_name().ljust(7) +
                  '\t' + str(ranking_system.get_rankings()[ranking].get_rating()).rjust(5))

        flag = easygui.buttonbox('请选择你要进行的操作', system_name, ['录入比赛结果', '新增选手', '退出系统'])

        if flag == '录入比赛结果':

            team1 = easygui.enterbox('请输入胜方当前的排名，不同选手间用小数点“.”隔开', flag, ).split('.')
            while not list_is_dig_list(team1):
                team1 = easygui.enterbox('输入非法，请重新输入胜方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
            for index in range(len(team1)):
                team1[index] = int(team1[index])
            while not list_is_key_list(team1, ranking_system.get_rankings()):
                team1 = easygui.enterbox('输入非法，请重新输入胜方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
            team1 = ranking_system.get_player_list_by_ranking_list(team1)

            team0 = easygui.enterbox('请输入败方当前的排名，不同选手间用小数点“.”隔开', flag).split('.')
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

            new_player_s_name = easygui.enterbox('输入新选手的姓名', flag)
            new_player_s_rating = easygui.enterbox('输入新选手的等级分（默认初始等级分为1370）', flag, default='1370')
            while not new_player_s_rating.isdigit():
                new_player_s_rating = easygui.enterbox('输入非法，请重新输入新选手的等级分（默认初始等级分为1370）',
                                                       flag, default='1370')
            new_player_s_rating = int(new_player_s_rating)
            ranking_system.add_player(Elo_Module.Player(new_player_s_name, new_player_s_rating))

        elif flag == '退出系统':

            if easygui.ccbox('是否保存修改', flag, ['是', '否']):
                player_data_write = []
                for player in ranking_system.get_player_list():
                    player_data_write.append(player.get_name() + '：' + str(player.get_rating()))
                if system_name == '单打排名':
                    txt_r_w.write_txt('Singles', player_data_write)
                    txt_r_w.write_txt('Singles' +
                                      time.strftime("%Y.%m.%d.%H-%M-%S", time.localtime()), player_data_write)
                elif system_name == '双打排名':
                    txt_r_w.write_txt('Doubles', player_data_write)
                    txt_r_w.write_txt('Doubles' +
                                      time.strftime("%Y.%m.%d.%H-%M-%S", time.localtime()), player_data_write)
                break
            else:
                break

    end = time.process_time()
    print(f'runtime = {end - start}')
