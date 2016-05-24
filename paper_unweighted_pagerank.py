# -*- coding: utf-8 -*-
"""
# 9
author: Zhong Peng
由author_paper5_abort_null.csv和all_information_2.csv创建的引用网络（边有权重）
在该引用网络中计算各个节点pagerank值，供下一步骤使用
与 # 6.1.3做对比，无权重
"""
from __future__ import division
import networkx as nx
import csv
import pagerank

# 构建网络
graph = nx.DiGraph()

# 得到所有信息全的论文的列表
all_realted_paper_li = list()
with open(r'..\result\all_related_paper_full_info.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_realted_paper_li.append(row[0])
print "all_realted_paper_li create over"
print "len(all_realted_paper_li):", len(all_realted_paper_li)

# 读取作者前五年论文
paper5_set = set()
with open(r'..\result\paper5.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in all_realted_paper_li:
            paper5_set.add(row[0])
print "paper5_set and paper5_li create over"
print "len(paper5_set):", len(paper5_set)

with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in paper5_set:
            graph.add_node(row[0])
            cite_paper_li = row[7][2: -2].split('\', \'')
            for cite_paper in cite_paper_li:
                if cite_paper in all_realted_paper_li:
                    graph.add_edge(row[0], cite_paper)
print "graph create over"
print graph.number_of_nodes()
print graph.number_of_edges()

rank_value = pagerank.pagerank(graph, max_iteration=1000)
pagerank.save_pagerank_value(rank_value, r'..\result\paper_unweighted_pagerank.csv')
