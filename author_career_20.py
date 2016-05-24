# -*- coding: utf-8 -*-
"""
# 1
author: Zhong Peng
由author_life.csv统计出学术生涯为20年的学者的名单存入author_career_20.csv
"""
import csv

author_li = list()
with open(r'..\g_result\author_life.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if int(row[1]) == 20:
            author_li.append(row)


with open(r'..\result\author_career_20.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(author_li)
