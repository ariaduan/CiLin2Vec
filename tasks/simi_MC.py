#coding:utf-8
from math import sqrt
import gensim
import sys
import importlib
importlib.reload(sys)
model = gensim.models.Word2Vec.load('../models/cb_cilin_def_palin_3.model')#replace this file with the one you want to use

file1 = open('../files/MC_words_pairs','rb')
fileout = open('../results/simi_MC_cb_cilin_def_palin_3','w',encoding = 'utf-8')#replace this file in correspondence with the name of file1

y = []

for line1 in file1:
    line1 = line1.decode('utf-8')
    tmp1 = line1.split()
    x1 = model.similarity(tmp1[0], tmp1[1])
    fileout.write(str(x1) + ',')
    y.append(x1)


 
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
 
x = [0.98,0.96,0.96,0.94,0.925,0.9025,0.875,0.855,0.7775,0.77,0.7625,0.7425,0.7375,0.705,0.42,0.415,0.29,0.275,0.2375,0.2225,0.2175,0.21,0.1575,0.1375,0.105,0.105,0.0325,0.0275,0.02,0.02]

print(corrcoef(x,y))

file1.close()
fileout.close()
