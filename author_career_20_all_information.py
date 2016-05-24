# -*- coding: utf-8 -*-
"""
# 3 abort
author: Zhong Peng
由author_career_20.csv, author_paper.csv以及all_information_2.csv生成
学术生涯20年的作者的全部信息author_career_20_all_info.csv
"""
import csv

# author_li是需要的作者的id列表
author_li = list()
with open(r'..\result\author_career_20.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        author_li.append(row[0])
print author_li[0]
print author_li[-1]

# author和paper对应的字典, paper是列表形式
author_paper_dic = dict()
with open(r'..\result\author_paper.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if author in author_li:
            paper_li = row[1][2:-2].split('\', \'')
            author_paper_dic[row[0]] = paper_li

# ???
paper_info_dic = dict()
with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

