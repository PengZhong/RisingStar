# -*- coding: utf-8 -*-
"""
# 6.1.0.1
author: Zhong Peng
由author_paper5_abort_null.csv和all_information_2.csv创建的引用网络（边有权重）
在该引用网络中计算各个节点pagerank值，供下一步骤使用
假设有边P1->P2，权重为P1中的一二作者以及P2中一二作者所有论文的所有keywords的余弦相似度
由于后续会用到venue信息，在此步骤中，所有涉及到的论文必须有venue信息
所有与引文网络相关的引用全部存入all_related_paper.csv
在6.1.0.0基础上，把所有信息从all_information_2.csv中提取出来，
去除信息不全的论文存入all_related_paper_full_info.csv
"""
import csv

all_related_paper_li = list()
with open(r'..\result\all_related_paper.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_related_paper_li.append(row[0])
print len(all_related_paper_li)

full_info_li = list()
with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in all_related_paper_li:
            if len(row) == 8:
                if row[5] != '':
                    full_info_li.append(row)
print len(full_info_li)

with open(r'..\result\all_related_paper_full_info.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(full_info_li)
print "file writes over"  # 1025行结果

# full_info_li = list()
# with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         if row[0] in all_related_paper_li:
#             if row[5] != '':
#                 full_info_li.append(row)
# print len(full_info_li)

# with open(r'..\result\all_related_paper_full_info2.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(full_info_li)
# print "file writes over"  # 1036行结果
