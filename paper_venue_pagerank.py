# -*- coding: utf-8 -*-
"""
# 8.2
author: Zhong Peng
构建paper-venue的无向图(有边权)，paepr的初始值从paper_author_pagerank.csv继承
venue的初始值 
本文件用来构造paper_venue的无向有权重网络，并计算各个节点的pagerank值，存入paper_venue_pagerank.csv
权重为论文引用量除以期刊引用量
"""
from __future__ import division
import csv
import networkx as nx


def paper_venue_pagerank(graph, venues, max_iterations, min_delta=0.0001, damping_factor=0.85):
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "empty graph"
        return {}

    # init step, venue值初始化为 1 / venue总数, paper从paper_author_pagerank.csv中继承
    rank = {}.fromkeys(venues, 1 / len(venues))
    paper_node_li = list()
    with open(r'..\result\paper_weighted_pagerank.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            paper_node_li.append(row[0])
    print "paper_node_li creates over"

    with open(r'..\result\paper_author_pagerank_value.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] in paper_node_li:
                rank[row[0]] = float(row[1])
    min_value = (1.0 - damping_factor) / graph.number_of_nodes()

    # iteration step
    for current_time in range(1, max_iterations + 1):
        print "iteration time: %s" % current_time
        diff = 0.0
        for node in nodes:
            rank_score = min_value
            for neighbor in graph.neighbors(node):
                # 获取pre_node到node的权重
                weight = graph.get_edge_data(neighbor, node)['weight']
                # 获取pre_node的全部出边的权重和
                weight_sum = 0
                for to_node in graph.neighbors(neighbor):
                    weight_sum += graph.get_edge_data(neighbor, to_node)['weight']
                rank_score += damping_factor * rank[neighbor] * weight / weight_sum
            diff += abs(rank_score - rank[node])
            rank[node] = rank_score
        if diff < min_delta:
            print "iteration converge in %s time" % current_time
            break
    return rank


def save_pagerank_value(rank, file_path):
    li = sorted(rank.iteritems(), key=lambda x: x[1], reverse=True)
    with open(file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(li)
    print "file writes over"


if __name__ == '__main__':
    
    paper_citation_dic = dict()
    with open(r'..\result\paper_citation_count.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            paper_citation_dic[row[0]] = int(row[1])
    print "paper_citation_dic creates over"

    venue_citation_dic = dict()
    venue_li = list()
    with open(r'..\result\venue_citation_count.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            venue_citation_dic[row[0]] = int(row[1])
            venue_li.append(row[0])
    print "venue_citation_dic creates over"
    print "venue_li creates over"

    # 创建网络
    graph = nx.Graph()
    count = 0
    with open(r'..\result\all_related_paper_full_info.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if paper_citation_dic.has_key(row[0]):
                count += 1
                paper_citations = paper_citation_dic[row[0]]
                venue_citations = venue_citation_dic[row[5]]
                graph.add_edge(row[0], row[5], {'weight': paper_citations / venue_citations})
    print "graph create over"
    print "count:", count

    # 计算pagerank值并存储
    rank_value = paper_venue_pagerank(graph, venues=venue_li, max_iterations=1000)
    file_path = r'..\result\paper_venue_pagerank.csv'
    save_pagerank_value(rank_value, file_path)
