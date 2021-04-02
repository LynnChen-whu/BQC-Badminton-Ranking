# -*- coding = utf-8 -*-
# @Time : 2021-2-7 15:01
# @Author : Lynn
# @File : txt_r_w.py
# @Software : PyCharm


def write_txt(name: str, content: list):
    if str(type(name)) == "<class 'str'>" and \
            str(type(content)) == "<class 'list'>":
        if name[-4:] == '.txt':
            file = open(name, 'w', encoding='utf8')
        else:
            file = open(name + '.txt', 'w', encoding='utf8')
        for sentence in content:
            if repr(sentence)[-3:-1] == r'\n':
                file.write(sentence)
            else:
                file.write(sentence + '\n')
        file.close()
        return 'success'
    else:
        print('传入函数“write_txt”的参数格式不正确')
        return 'fail'


def read_lines_from_txt(name: str) -> list or str:
    if str(type(name)) == "<class 'str'>":
        if name[-4:] == '.txt':
            try:
                file = open(name, 'r', encoding='utf8')
            except IOError as err_info:
                print(f'打开文件"{name}"时出错\n' + repr(err_info))
                return 'fail'
        else:
            try:
                file = open(name + '.txt', 'r', encoding='utf8')
            except IOError as err_info:
                print(f'打开文件"{name}"时出错\n' + repr(err_info))
                return 'fail'
        return file.readlines()
    else:
        print('传入函数“read_lines_from_txt”的参数格式不正确')
        return 'fail'


def copy_txt1_to_txt2(name1: str, name2: str):
    if write_txt(name2, read_lines_from_txt(name1)) == 'success':
        print('复制成功')
    else:
        print('操作失败')



