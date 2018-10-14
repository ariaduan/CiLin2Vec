import gensim
from gensim.test.utils import datapath
from gensim.models import KeyedVectors
import numpy as np
import torch
from argparse import ArgumentParser
from math import sqrt

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

def multipl(a,b):
    sumofab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab
 
def corrcoef(x,y):
    n=len(x)
    sum1=sum(x)
    sum2=sum(y)
    sumofxy=multipl(x,y)
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    return num/den

for model in models:
    embeddings = KeyedVectors.load_word2vec_format(datapath(("../models/{}.model".format(model))), binary = True)
    MC_sem1 = open('../files/MC_sememes_1','rb')
    MC_sem2 = open('../files/MC_sememes_2','rb')
    MC_pairs = open('../files/MC_words_pairs','rb')
    fileout = open('../results/sem_simi_MC_' + model,'w',encoding = 'utf-8')
    
    y = []
    score = []
    for sem1 in MC_sem1:
        sem1 = sem1.decode('utf-8').split()
        sem2 = MC_sem2.readline().decode('utf-8').split()
        if sem1[0] == '&':
            m = max(score)
            pair = MC_pairs.readline().decode("utf-8").split()
            fileout.write(pair[0] + '\t' + pair[1] + '\t' + str(m) + '\n')
            y.append(m)
            score = []
            continue
        length1 = len(sem1)
        length2 = len(sem2)
        semvec1 = np.mat(0)
        semvec2 = np.mat(0)
        for i in range(len(sem1)):
            tmp = multi_vec(embeddings[sem1[i]],1/(2**(i+1))) if (i != (len(sem1)-1)) else multi_vec(embeddings[sem1[i]],1/(2**i))
            semvec1 = semvec1 + np.mat(tmp)
        for i in range(len(sem2)):
            tmp = multi_vec(embeddings[sem2[i]],1/(2**(i+1))) if (i != (len(sem2)-1)) else multi_vec(embeddings[sem2[i]],1/(2**i))
            semvec2 = semvec2 + np.mat(tmp)
    
        total = cos_sim(semvec1,semvec2)
        score.append(total)
     
    x = [0.98,0.96,0.96,0.94,0.925,0.9025,0.875,0.855,0.7775,0.77,0.7625,0.7425,0.7375,0.705,0.42,0.415,0.29,0.275,0.2375,0.2225,0.2175,0.21,0.1575,0.1375,0.105,0.105,0.0325,0.0275,0.02,0.02]
    
    print(corrcoef(x,y))
    fileout.write(str(corrcoef(x,y)) + '\n')
    
    MC_sem2.close()
    MC_sem1.close()
    MC_pairs.close()
    fileout.close()
