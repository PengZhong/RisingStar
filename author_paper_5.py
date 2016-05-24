# -*- coding: utf-8 -*-
"""
# 4
author: Zhong Peng
由author_paper.csv以及all_information_2.csv生成
学术生涯20年的作者的前五年的作者论文对应，存入paper_5.csv, 以及author_paper5.csv
"""
import csv

# author id(学术生涯20年的学者)的列表和所有paper的列表以及作者论文对应的字典{author: [papers]}
author_li = list()
all_paper_li = list()
author_paper_dic = dict()
with open(r'..\result\author_paper_20y.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        author_li.append(row[0])
        paper_li = row[1][2:-2].split('\', \'')
        all_paper_li.extend(paper_li)
        author_paper_dic[row[0]] = paper_li
all_paper_li = list(set(all_paper_li))
print "len(author_li)", len(author_li)
print "len(all_paper_li)", len(all_paper_li)
print "len(author_paper_dic.keys())", len(author_paper_dic.keys())
print "author_paper_dic create over"


# author id与其学术生涯起始年份对应的字典{author: year}
author_year_dic = dict()
with open(r'..\g_result\author_year.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in author_li:
            year_li = row[1][2:-2].split('\', \'')
            year_li = map(int, year_li)
            year_li.sort()
            author_year_dic[row[0]] = year_li[0]
print "len(author_year_dic.keys())", len(author_year_dic.keys())
print "author_year_dic create over"


# paper id和其年份对应的字典{paper: year}
paper_year_dic = dict()
with open(r'..\g_result\all_information_2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in all_paper_li:
            paper_year_dic[row[0]] = int(row[3])
# print paper_year_dic[row[0]]
print "len(paper_year_dic.keys())", len(paper_year_dic.keys())
print "paper_year_dic create over"


# 筛选author_paper_dic中的paper，留下前五年的
final_author_paper_dic = {}.fromkeys(author_li)
final_paper_li = list()
for k, v in author_paper_dic.iteritems():    # k是作者，v是论文列表
    year = author_year_dic[k]
    for paper in v:
        if (paper_year_dic[paper] - year) < 5:
            if final_author_paper_dic[k] == None:
                final_author_paper_dic[k] = [paper]
                final_paper_li.append([paper])
            else:
                final_author_paper_dic[k].append(paper)
                final_paper_li.append([paper])
print "len(final_paper_li)", len(final_paper_li)
print "final_paper_li create over"
print "len(final_author_paper_dic.keys())", len(final_author_paper_dic.keys())
print "final_author_paper_dic create over"


with open(r'..\result\paper5.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(final_paper_li)
print "final_paper_li writes over"


items = final_author_paper_dic.items()
items.sort(key=lambda x: author_li.index(x[0]))
with open(r'..\result\author_paper5.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(items)
print "final_author_paper_dic writes over"
