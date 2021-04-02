# -*- coding = utf-8 -*-
# @Time : 2021-4-2 14:29
# @Author : Lynn
# @File : UI.py
# @Software : PyCharm

import time
import Elo_Module
import txt_r_w
import easygui

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
        player_data_temp = item.split('：')  # 数据格式是“名字：等级分”，冒号是中文字符
        player_list.append(Elo_Module.Player(player_data_temp[0], int(player_data_temp[1])))
    ranking_system = Elo_Module.Ranking_System(name, player_list)

    while 1:
        print(f'当前{name}情况如下')
        ranking_list = list(ranking_system.get_rankings().keys())
        ranking_list.sort()
        for ranking in ranking_list:
            print(str(ranking).rjust(3) + '\t' + ranking_system.)

        flag = easygui.buttonbox('请选择你要进行的操作', name, ['查看排名', '录入比赛结果', '新增选手', '退出系统'])

    end = time.process_time()
    print(f'runtime = {end - start}')
