#coding:utf-8
from math import sqrt
import gensim
import sys
import importlib
importlib.reload(sys)
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument("--models", action = "append", type = str)
args = p.parse_args()
models = args.models

for m in models:
	model = gensim.models.Word2Vec.load('../models/' + m + '.model')
	MC_pairs = open('../files/MC_words_pairs','rb')
	fileout = open('../results/simi_MC_' + m,'w',encoding = 'utf-8')
	
	y = []
	
	for pair in MC_pairs:
	    pair = pair.decode('utf-8').split()
	    tmp = model.similarity(pair[0], pair[1])
	    fileout.write(pair[0] + '\t' + pair[1] + '\t' + str(tmp) + '\n')
	    y.append(tmp)
		 
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
	fileout.write(str(corrcoef(x,y)) + '\n')
	
	MC_pairs.close()
	fileout.close()
