# -*- coding: utf-8 -*-
"""
# 6
author: Zhong Peng
由author_paper5_abort_null.csv和all_information_2.csv创建的引用网络（边无权重）
在该引用网络中计算各个节点pagerank值，供下一步骤使用
"""
import csv
import networkx as nx
import pagerank

all_paper_list = list()
with open(r'..\result\paper5.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_paper_list.append(row[0])


graph = nx.DiGraph()
with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in all_paper_list:
            if len(row) == 8:
                cite_paper_str = row[7]
                if cite_paper_str == '[]':
                    graph.add_node(row[0])
                else:
                    cite_paper_li = cite_paper_str[2: -2].split('\', \'')
                    for cite_paper in cite_paper_li:
                        graph.add_edge(cite_paper, row[0])
            else:
                graph.add_node(row[0])
print "graph create over"


rank_value_dic = pagerank.pagerank(graph, 1000)

file_path = r'..\result\paper_pagerank_value.csv'
pagerank.save_pagerank_value(rank_value_dic, file_path)
