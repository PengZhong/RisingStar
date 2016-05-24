# -*- coding: utf-8 -*-
"""
pagerank算法的实现
"""
from __future__ import division
import networkx as nx
import csv

def pagerank(graph, max_iteration, min_delta=0.0001, damping_factor=0.85):
    '''pagerank in directed graph, return {node: value} dictionary'''
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "empty graph"
        return {}
    rank = {}.fromkeys(nodes, 1.0 / graph_size)
    min_value = (1.0-damping_factor) / graph_size

    for current_time in range(1, max_iteration + 1):
        print "iteration time: %s" % current_time
        diff = 0.0
        for node in nodes:
            rank_score = min_value
            for pre_node in graph.predecessors(node):
                rank_score += damping_factor * rank[pre_node] / len(graph.successors(pre_node))
            diff += abs(rank[node] - rank_score)
            rank[node] = rank_score
        if diff < min_delta:
            print "converge in iteration time:", current_time
            break
    print "pagerank algorithm over"
    return rank


def save_pagerank_value(rank, file_path):
    items = sorted(rank.iteritems(), key=lambda x: x[1], reverse=True)
    with open(file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(items)
    print "pagerank value saved"

