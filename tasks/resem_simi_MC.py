import numpy as np
from math import sqrt


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



file1 = open('../models/cb_cilin_def_palin_3.vector','rb')#replace this file with the one you want to use
file2 = open('../files/MC_sememes_1','rb')
file3 = open('../files/MC_sememes_2','rb')
fileout = open('../results/resem_simi_MC_cb_cilin_def_palin_3','w',encoding = 'utf-8')#replace this file in correspondence with the name of file1

line1 = file1.readline()

bank = []
vec = []
for line1 in file1:
    line1 = line1.decode('utf-8')
    tmp1 = line1.split()
    bank.append(tmp1[0])
    vec.append(list(map(float,tmp1[1:])))

 
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

y = []
score = []
for line2 in file2:
    line2 = line2.decode('utf-8')
    tmp2 = line2.split()
    line3 = file3.readline().decode('utf-8')
    tmp3 = line3.split()
    if tmp2[0] == '&':
        m = max(score)
        fileout.write(str(m) + ',')
        y.append(m)
        score = []
        continue
    length1 = len(tmp2)
    length2 = len(tmp3)
    semvec1 = np.mat(0)
    semvec2 = np.mat(0)
    for i in range(len(tmp2)-1,-1,-1):
        ix = bank.index(tmp2[i])
        tmp = multi_vec(vec[ix],1/(2**(len(tmp2)-i))) if (i != 0) else multi_vec(vec[ix],1/(2**(len(tmp2)-i-1)))
        semvec1 = semvec1 + np.mat(tmp)
    for i in range(len(tmp3)-1,-1,-1):
        ix = bank.index(tmp3[i])
        tmp = multi_vec(vec[ix],1/(2**(len(tmp3)-i))) if (i != 0) else multi_vec(vec[ix],1/(2**(len(tmp3)-i-1)))
        semvec2 = semvec2 + np.mat(tmp)

    total = cos_sim(semvec1,semvec2)
    score.append(total)

print(corrcoef(x,y))


file1.close()
file2.close()
file3.close()
fileout.close()