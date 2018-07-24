import numpy as np


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
fileout = open('../results/sem_simi_MC_cb_cilin_def_palin_3','w',encoding = 'utf-8')#replace this file in correspondence with the name of file1

line1 = file1.readline()

bank = []
vec = []
for line1 in file1:
    line1 = line1.decode('utf-8')
    tmp1 = line1.split()
    bank.append(tmp1[0])
    vec.append(list(map(float,tmp1[1:])))

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
    for i in range(len(tmp2)):
        ix = bank.index(tmp2[i])
        tmp = multi_vec(vec[ix],1/(2**(i+1))) if (i != (len(tmp2)-1)) else multi_vec(vec[ix],1/(2**i))
        semvec1 = semvec1 + np.mat(tmp)
    for i in range(len(tmp3)):
        ix = bank.index(tmp3[i])
        tmp = multi_vec(vec[ix],1/(2**(i+1))) if (i != (len(tmp3)-1)) else multi_vec(vec[ix],1/(2**i))
        semvec2 = semvec2 + np.mat(tmp)

    total = cos_sim(semvec1,semvec2)
    score.append(total)


from math import sqrt
 
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
file3.close()
file2.close()
fileout.close()