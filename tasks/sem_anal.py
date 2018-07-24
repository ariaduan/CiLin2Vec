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
file2 = open('../files/anal_cilin','rb')
file3 = open('../files/cilin_hier_perword','rb')
fileout = open('../results/sem_anal_cb_cilin_def_palin_3','w',encoding = 'utf-8')#replace this file in correspondence with the name of file1

line1 = file1.readline()

bank = []
vec = []
for line1 in file1:
    line1 = line1.decode('utf-8')
    tmp1 = line1.split()
    bank.append(tmp1[0])
    vec.append(list(map(float,tmp1[1:])))


sems = []
words = []

for line3 in file3:
    line3 = line3.decode('utf-8')
    tmp3 = line3.split()
    words.append(tmp3[5])
    sems.append(tmp3[:5])


def semword(word):
    ide = words.index(word)
    sem = sems[ide]
    length1 = len(sem)
    semvec1 = np.mat(0)
    for i in range(len(sem)):
        ix = bank.index(sem[i])
        tmp = multi_vec(vec[ix],1/(2**(i+1))) if (i != (len(sem)-1)) else multi_vec(vec[ix],1/(2**i))
        semvec1 = semvec1 + np.mat(tmp)
    return semvec1



num = 0.0
cnt = 0
for line2 in file2:
    line2 = line2.decode('utf-8')
    tmp2 = line2.split()
    #0-2+3=1
    vec0 = semword(tmp2[0])
    vec1 = semword(tmp2[1])
    vec2 = semword(tmp2[2])
    vec3 = semword(tmp2[3])
    tmp = vec0 + vec3 - vec2
    score = cos_sim(vec1,tmp)
    num += score
    cnt += 1
print(num/cnt)

fileout.close()
file1.close()
file2.close()
file3.close()