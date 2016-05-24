# -*- coding: utf-8 -*-
"""
# 11
author: Zhong Peng
构建paper-venue的无向图(有边权)，paepr的初始值从paper_author_pagerank.csv继承
venue的初始值 
本文件用来构造paper_venue的无向有权重网络，并计算各个节点的pagerank值，存入paper_venue_pagerank.csv
无权重，与# 8.2做对比
"""
from __future__ import division
import csv
import networkx as nx


def unweighted_pagerank(graph, venues, max_iterations, min_delta=0.0001, damping_factor=0.85):
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "empty graph"
        return {}

    rank = {}.fromkeys(venues, 1 / len(venues))
    paper_node_li = list()
    with open(r'..\result\paper_unweighted_pagerank.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            paper_node_li.append(row[0])
    print "paper_node_li creates over"

    with open(r'..\result\paper_author_unweighted_pagerank.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] in paper_node_li:
                rank[row[0]] = float(row[1])
    min_value = (1.0 - damping_factor) / graph.number_of_nodes()
    print graph_size == len(rank.keys())

    for current_time in range(1, max_iterations + 1):
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
    # 创建网络
    graph = nx.Graph()

    # 获取论文列表
    paper_li = list()
    with open(r'..\result\paper_unweighted_pagerank.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            paper_li.append(row[0])
    print "paper_li creates over"
    print "len(paper_li):", len(paper_li)

    # 创建期刊列表
    venue_li = list()
    with open(r'..\result\venue_citation_count.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            venue_li.append(row[0])
    print "venue_li creates over"

    count = 0
    with open(r'..\result\all_related_paper_full_info.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] in paper_li:
                count += 1
                graph.add_edge(row[0], row[5])
    print "graph create over"
    print "count:", count

    # 计算pagerank值并存储
    rank_value = unweighted_pagerank(graph, venues=venue_li, max_iterations=1000)
    file_path = r'..\result\paper_venue_unweighted_pagerank.csv'
    save_pagerank_value(rank_value, file_path)
