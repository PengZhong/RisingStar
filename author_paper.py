# -*- coding: utf-8 -*-
"""
# 2
author: Zhong Peng
由all_information_2.csv生成学者与论文相对应的文件并存入author_paper.csv中
"""
import csv

author_paper_dic = dict()
with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        paper = row[0]
        author_col = row[6][2:-2]
        if author_col == '':
            continue
        else:
            author_li = author_col.split('\', \'')
        for author in author_li:
            if author_paper_dic.has_key(author):
                author_paper_dic[author].append(paper)
            else:
                author_paper_dic[author] = [paper]
print "author_paper_dic created over"

with open(r'..\result\author_paper.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(author_paper_dic.iteritems())
