# -*- coding: utf-8 -*-
"""
# 6.1.3
author: Zhong Peng
由author_paper5_abort_null.csv和all_information_2.csv创建的引用网络（边有权重）
在该引用网络中计算各个节点pagerank值，供下一步骤使用
假设有边P1->P2，权重为P1中的一二作者以及P2中一二作者所有论文的所有keywords的LDA相似度
此文件根据6.1.1中生成的文件创立有向图(有权重)并计算pagerank值存入paper_weighted_pagerank.csv
"""
from __future__ import division
import networkx as nx
import csv
import cosine_similarity


def weighted_pagerank(graph, max_iteration, min_delta=0.0001, damping_factor=0.85):
    """带边权的引文网络中计算pagerank"""
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "empty graph"
        return {}

    # 初始化
    rank = {}.fromkeys(nodes, 1.0 / graph_size)
    min_value = (1-damping_factor) / graph_size

    # pagerank值更新
    for current_time in range(1, max_iteration + 1):
        print "iteration time:", current_time
        diff = 0.0
        for node in nodes:
            rank_score = min_value
            for pre_node in graph.predecessors(node):
                # 获取pre_node到node的权重
                weight = graph.get_edge_data(pre_node, node)['weight']
                # 获取pre_node的全部出边的权重和
                sum_weight = 0
                for to_node in graph.successors(pre_node):
                    sum_weight += graph.get_edge_data(pre_node, to_node)['weight']
                rank_score += damping_factor * rank[pre_node] * weight / sum_weight
            diff += abs(rank_score - rank[node])
            rank[node] = rank_score
        if diff < min_delta:
            print "pagerank converge in iteration time", current_time
            break
    return rank


def save_pagerank_value(rank, file_path):
    items = sorted(rank.iteritems(), key=lambda x: x[1], reverse=True)
    with open(file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(items)
    print "file write over"


if __name__ == '__main__':
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

    # 获取论文-关键词字典
    paper_keyword_dic = dict()
    with open(r'..\g_result\keyword.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] in all_realted_paper_li:
                paper_keyword_dic[row[0]] = row[1][2: -2].split('\', \'')
    print "paper_keyword_dic create over"
    print "len(paper_keyword_dic.keys()):", len(paper_keyword_dic.keys())

    with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] in paper5_set:
                graph.add_node(row[0])
                cite_paper_li = row[7][2: -2].split('\', \'')
                for cite_paper in cite_paper_li:
                    if cite_paper in all_realted_paper_li:
                        li1 = paper_keyword_dic[row[0]]
                        li2 = paper_keyword_dic[cite_paper]
                        edge_weight = cosine_similarity.sim_simulation(li1, li2)
                        graph.add_edge(row[0], cite_paper, {'weight': edge_weight})
    print "graph create over"
    print graph.number_of_nodes()
    print graph.number_of_edges()

    # 计算pagerank值
    rank_value = weighted_pagerank(graph, max_iteration=1000)

    # 存储pagerank值
    save_pagerank_value(rank_value, r'..\result\paper_weighted_pagerank.csv')
