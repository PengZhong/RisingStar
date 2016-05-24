# -*- coding: utf-8 -*-
"""
# 6.1.1
author: Zhong Peng
由author_paper5_abort_null.csv和all_information_2.csv创建的引用网络（边有权重）
在该引用网络中计算各个节点pagerank值，供下一步骤使用
假设有边P1->P2，权重为P1中的一二作者以及P2中一二作者所有论文的所有keywords的余弦相似度
本文件主要统计论文的keywords对应的文件，
使用all_related_paper_full_info.csv以及keyword.csv生成all_related_paper_keywords.csv
"""
import csv

paper_li = list()
with open(r'..\result\all_related_paper_full_info.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        paper_li.append(row[0])
print "paper_li create over"
print len(paper_li)
print len(set(paper_li))

author_keywords = list()
with open(r'..\g_result\keyword.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in paper_li:
            keywords = row[1][2: -2].split('\', \'')
            author_keywords.append((row[0], keywords))
print "author_keywords create over"
print len(author_keywords)

with open(r'..\result\all_related_paper_keywords.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(author_keywords)
print "file writes over"
