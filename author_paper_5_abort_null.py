# -*- coding: utf-8 -*-
"""
# 5
author: Zhong Peng
将author_paper5.csv中第二列为空的去掉
"""
import csv

author_paper_dic = dict()
author_li = list()
with open(r'..\result\author_paper5.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] == '':
            continue
        else:
            paper_li = row[1][2: -2].split('\', \'')
            author_paper_dic[row[0]] = paper_li
            author_li.append(row[0])
print "author_paper_dic create over"


items = author_paper_dic.items()
items.sort(key=lambda x: author_li.index(x[0]))
with open(r'..\result\author_paper5_abort_null.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(items)
print "file write over"
