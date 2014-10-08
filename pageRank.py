import random
import math
import sys
import numpy as np

# @param M: numpy array of adjacency matrix where M_ij represents the link from j to i such that sum(i,M_ij)=1 for all j
# @param d: damping factor
# @param thres: quadratic error threshold
# @return v: a vector of ranks such that v_i is the ith rank from [0, 1]
def pageRank(M, d, thresh):
    N = len(M[0])
    # initialization of v
    # can use all equal probabilities v = np.array([1./N for i in range(N)])
    # or random probabilities
    v = np.array([random.random() for i in range(N)])
    v = v/sum(v)
    vPre = np.array([sys.maxint for i in range(N)]) 
    M_hat = d*M + (1-d)/N * np.ones([N,N])

    # power iteration, minimizing l1 error: sum(abs(v-vPre)) or l2 error 
    while math.sqrt(sum(abs(v-vPre)**2)) > thresh:
        vPre = v
        v = np.dot(M_hat, v)

    return v


# @param M: dictionary of non-zero elements in the adjacency matrix where key is the row number, value is tupe(col number,element value), assuming M is valid 
# @param d: damping factor
# @param thres: quadratic error threshold
# @param num: number of links
# @return v: a dictionary of ranks where key is the idex of a link, value is the rank measure
def pageRankSparse(M, d, thresh, num):
    # equal probability initialization
    v = np.ones(num)*1./num
    err  = sys.maxint

    while err > thresh:
        vPre = np.copy(v)
        for key in M:
            v[key] = sum([ d*elem[1]*v[elem[0]] for elem in M[key]])        
            v[key]+= (1-d)*1./num 
        err = math.sqrt(sum(abs(v-vPre)**2)) 

    return v


# @param M: numpy array of adjacency matrix where M_ij represents the link from j to i such that sum(i,M_ij)=1 for all j
# @param idx: an int, index of the link to be tweaked
# @param idxIncrease: an int, index of the link to be increased (or decreased)
# @percentage: a float, percentage of increase in transitional probability (decrease if negative)
def tweakM(M,idx,idxIncrease,increase):
    if M[idxIncrease][idx]==0:
        M[idxIncrease][idx] = delta =  increase
    else:
        delta = M[idxIncrease][idx]*increase 
        M[idxIncrease][idx] += delta
 
    for i in range(len(M)):
        if i!=idxIncrease and M[i][idx] != 0:
            M[i][idx] -= delta*M[i][idx]/(1-M[idxIncrease][idx]+delta)

    return M        


M = np.asarray([[0, 0, 0, 0, 1], [ 0.5, 0, 0, 0, 0], [0.5, 0, 0, 0, 0], [ 0, 1, 0.5, 0, 0],[0, 0, 0.5, 1, 0]])
print pageRank(M, 0.8, 0.001)

Msparse = {}
Msparse[0] = [[4,1]]
Msparse[1] = [[0,0.5]]
Msparse[2] = [[0,0.5]]
Msparse[3] = [[1,1],[2,0.5]]
Msparse[4] = [[2,0.5],[3,1]]
print pageRankSparse(Msparse, 0.8, 0.001, 5)

Mtweak = tweakM(M,0,1,0.2)
print Mtweak
print pageRank(Mtweak, 0.8, 0.001)
