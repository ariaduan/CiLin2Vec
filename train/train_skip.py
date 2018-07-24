#coding:utf-8
import logging
import os.path
import sys
import gensim
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
inp = '../files/cilin_hier_perword'
outp1 = '../models/sg_cilin_def_palin_3.model'
outp2 = '../models/sg_cilin_def_palin_3.vector'
model = Word2Vec(LineSentence(inp), sg=1,size=300, window=3, min_count=0,\
                     workers=multiprocessing.cpu_count(),\
                     iter = 5)#adjust the parameters to get different models
model.save(outp1)
model.wv.save_word2vec_format(outp2, binary=False)