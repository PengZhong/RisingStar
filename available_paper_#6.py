# -*- coding: utf-8 -*-
"""
# 6.1.0.0
author: Zhong Peng
由author_paper5_abort_null.csv和all_information_2.csv创建的引用网络（边有权重）
在该引用网络中计算各个节点pagerank值，供下一步骤使用
假设有边P1->P2，权重为P1中的一二作者以及P2中一二作者所有论文的所有keywords的余弦相似度
由于后续会用到venue信息，在此步骤中，所有涉及到的论文必须有venue信息
所有与引文网络相关的引用全部存入all_related_paper.csv
"""
import csv

all_paper_set = set()
with open(r'..\result\paper5_all_info.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_paper_set.add(row[0])
        if len(row) == 8:
            cite_paper_str = row[7]
            if not(cite_paper_str == '[]'):
                cite_paper_li = cite_paper_str[2: -2].split('\', \'')
                all_paper_set.update(cite_paper_li)
print len(all_paper_set)
all_related_paper_li = [(elem, ) for elem in all_paper_set]
print len(all_related_paper_li)

with open(r'..\result\all_related_paper.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_related_paper_li)
