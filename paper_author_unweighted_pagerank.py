# -*- coding: utf-8 -*-
"""
# 10
author: Zhong Peng
构建paper-author的无向图(有边权)，paepr的初始值从paper_pagerank.py继承
author的初始值为作者总数分之一
假设有a1<->p1的边, 无权重与# 7做对比
"""
from __future__ import division
import csv
import networkx as nx


def unweighted_pagerank(graph, max_iteration, author_li, min_delta=0.0001, damping_factor=0.85):
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "empty graph"
        return {}

    rank = {}.fromkeys(author_li, 1.0 / len(author_li))
    with open(r'..\result\paper_unweighted_pagerank.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rank[row[0]] = float(row[1])
    min_value = (1.0 - damping_factor) / graph.number_of_nodes()

    for current_time in range(1, max_iteration + 1):
        print "this is iteration time %s" % current_time
        diff = 0.0
        for node in nodes:
            rank_score = min_value
            for neighbor in graph.neighbors(node):
                rank_score += damping_factor * rank[neighbor] / len(graph.neighbors(neighbor))
            diff += abs(rank[node] - rank_score)
            rank[node] = rank_score
        if diff < min_delta:
            print "unweighted pagerank converged in iteration times: ", current_time
            break
    return rank


def save_pagerank_value(rank, file_path):
    items = sorted(rank.iteritems(), key=lambda x: x[1], reverse=True)
    with open(file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(items)
    print "file write over"


if __name__ == '__main__':
    # 构建一个无向网络
    graph = nx.Graph()

    # 获取全部论文节点
    paper_nodes_li = list()
    with open(r'..\result\paper_unweighted_pagerank.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            graph.add_node(row[0])
            paper_nodes_li.append(row[0])
    print "add paper nodes over"
    print "paper_nodes_li create over"

    # 论文-作者对应字典, 以及全部作者集合
    paper_author_dic = dict()
    all_author_set = set()
    with open(r'..\result\all_related_paper_full_info.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            author_list = row[6][2: -2].split('\', \'')
            paper_author_dic[row[0]] = author_list
            all_author_set.update(author_list)
    print "paper_author_dic create over"
    print "len(paper_author_dic):", len(paper_author_dic.keys())

    # 构建网络
    for pa in paper_nodes_li:
        authors = paper_author_dic[pa]  # 论文pa的全部作者列表
        for au in authors:
            graph.add_edge(pa, au)
    print "node numbers: ", graph.number_of_nodes()
    print "edge numbers: ", graph.number_of_edges()

    # 计算并存储pagerank值
    rank_value = unweighted_pagerank(graph, max_iteration=1000, author_li=list(all_author_set))
    save_pagerank_value(rank_value, r'..\result\paper_author_unweighted_pagerank.csv')
