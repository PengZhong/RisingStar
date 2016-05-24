# -*- coding: utf-8 -*-
"""
# 3
author: Zhong Peng
由author_paper.csv和author_career_20.csv生成
学术生涯20年的作者与论文对应的文件author_paper_20y.csv
"""
import csv

author_li = list()
with open(r'..\result\author_career_20.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        author_li.append(row[0])
print "author_li create over"


author_paper_dic = {}.fromkeys(author_li, list())
with open(r'..\result\author_paper.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if author_paper_dic.has_key(row[0]):
            paper_li = row[1][2: -2].split('\', \'')
            author_paper_dic[row[0]] = paper_li
print "author_paper_dic create over"


items = author_paper_dic.items()
print items[0]
print type(items)
items.sort(key=lambda x: author_li.index(x[0]))


with open(r'..\result\author_paper_20y.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(items)
print "write over"

