import gensim
from gensim.test.utils import datapath
from gensim.models import KeyedVectors
import numpy as np
import torch
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument("--models", action = "append", type = str)
args = p.parse_args()
models = args.models

def cos_sim(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim
'''
Author：衣介书生
Link：https://www.jianshu.com/p/0c33c17770a0
'''

def multi_vec(vector_a,x):
    vector_a = np.mat(vector_a)
    return vector_a*x

for model in models:
    embeddings = KeyedVectors.load_word2vec_format(datapath(("../models/{}.model".format(model))), binary = True)

    cilin = open('../files/cilin_hier_perword','rb')
    fileout = open('../results/sem_comp_' + model,'w',encoding = 'utf-8')
    
    scores = 0.0
    cnt = 0
    for line in cilin:
        line = line.decode('utf-8').split()
        word = line[5]
        sem = line[:5]
        length1 = len(sem)
        semvec1 = np.mat(0)
        for i in range(len(sem)):
            tmp = multi_vec(embeddings[sem[i]],1/(2**(i+1))) if (i != (len(sem)-1)) else multi_vec(embeddings[sem[i]],1/(2**i))
            semvec1 = semvec1 + np.mat(tmp)
        wordvec = np.mat(embeddings[word])
    
        score = cos_sim(wordvec,semvec1)
        for i in line:
            fileout.write(i + '\t')
        fileout.write(str(score) + '\n')
    
        scores += score
        cnt += 1
    
    print(scores/cnt)
    fileout.write("all:\t" + str(scores/cnt))
    
    fileout.close()
    cilin.close()
