# -*- coding: utf-8 -*-
"""
# 8.1
author: Zhong Peng
构建paper-venue的无向图(有边权)，paepr的初始值从paper_author_pagerank.csv继承
venue的初始值 
本文件用来统计选取出的paper的相关信息以及所涉及的venue的引用数量，所有信息统计自all_information2.csv
统计paper和venue的引用数量存入paper_citation_count.csv和venue_citation_count.csv
"""
import csv

all_paper_li = list()
with open(r'..\result\paper_weighted_pagerank.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_paper_li.append(row[0])
print "all_paper_li create over"
print "len(all_paper_li):", len(all_paper_li)

paper_cite_paepr_dic = dict()
venue_cite_paper_dic = dict()
with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in all_paper_li:
            cite_paper_li = row[7][2: -2].split('\', \'')
            paper_cite_paepr_dic[row[0]] = cite_paper_li
            if venue_cite_paper_dic.has_key(row[5]):
                venue_cite_paper_dic[row[5]].update(cite_paper_li)
            else:
                venue_cite_paper_dic[row[5]] = set(cite_paper_li)
print "paper_cite_paepr_dic create over"
print "len(paper_cite_paepr_dic):", len(paper_cite_paepr_dic.keys())
print "venue_cite_paper_dic create over"
print "len(venue_cite_paper_dic):", len(venue_cite_paper_dic.keys())

paper_citation_count_li = [(k, len(v)) for k, v in paper_cite_paepr_dic.iteritems()]
venue_citation_count_li = [(k, len(v)) for k, v in venue_cite_paper_dic.iteritems()]

with open(r'..\result\paper_citation_count.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(paper_citation_count_li)
print "paper_citation_count_li writes over"

with open(r'..\result\venue_citation_count.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(venue_citation_count_li)
print "venue_citation_count_li writes over"


# # 获取选取的论文列表
# paper_li = list()
# with open(r'..\result\paper5_keywords.csv', 'rb') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         paper_li.append(row[0])
# print len(paper_li)

# # 生成选取的论文的完整信息列表
# paper5_info_li = list()
# with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         if row[0] in paper_li:
#             paper5_info_li.append(row)
# print len(paper5_info_li)

# # 将上步生成的选取论文的完整信息写入文件
# with open(r'..\result\paper5_all_info.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(paper5_info_li)
# print "file writes over"

