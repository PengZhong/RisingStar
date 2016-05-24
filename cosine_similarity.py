# -*- coding: utf-8 -*-
"""
# 6.1.2
author: Zhong Peng
由author_paper5_abort_null.csv和all_information_2.csv创建的引用网络（边有权重）
在该引用网络中计算各个节点pagerank值，供下一步骤使用
假设有边P1->P2，权重为P1中的一二作者以及P2中一二作者所有论文的所有keywords的余弦相似度
本文件实现了余弦相似度的计算, 将作为依赖包使用
"""
from __future__ import division
import math
# from gensim import corpora, models, similarities
# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# texts = list()
# with open(r'..\result\paper5_keywords.csv', 'rb') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         keywords = row[1][2: -2].split('\', \'')
#         texts.append(keywords)
# print "texts create over"

# dictionary = corpora.Dictionary(texts)
# corpus = [dictionary.doc2bow(text) for text in texts]

# tfidf = models.TfidfModel(corpus)
# corpus_tfidf = tfidf[corpus]
# print tfidf
# print corpus_tfidf

# lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=20)
# corpus_lda = lda[corpus_tfidf]

# index = similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=20)
# sims = index[tfidf[vec]]
# print lsit(enumerate(sims))


def sim_simulation(li1, li2):
    """li1和li2是词列表"""
    word_set = set()
    word_set.update(li1)
    word_set.update(li2)
    li1_count = [li1.count(elem) for elem in word_set]
    li2_count = [li2.count(elem) for elem in word_set]
    # 分子
    num1 = sum(map(lambda x, y: x * y, li1_count, li2_count))
    # 分母
    tmp1 = [elem * elem for elem in li1_count]
    tmp2 = [elem * elem for elem in li2_count]
    num2 = math.sqrt(sum(tmp1)) * math.sqrt(sum(tmp2))
    return num1 / num2


if __name__ == '__main__':
    # sim_simulation测试部分
    str1 = "I like watching TV dont like watching movie"
    str2 = "I dont like watching TV dont like watching movie too"
    sentence1 = str1.split()
    sentence2 = str2.split()
    # texts = []
    # texts.append(sentence1)
    # texts.append(sentence2)
    print sim_simulation(sentence1, sentence2)
