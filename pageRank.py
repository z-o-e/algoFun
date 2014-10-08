import random
import math
import sys
import numpy as np
# @param M: numpy array of adjacency matrix where M_ij represents the link from j to i such that sum(i,M_ij)=1 for all j
# @param d: damping factor
# @param thres: quadratic error threshold
# @param quadraticErr: quadratic error for v
# @return v: a vector of ranks such that v_i is the ith rank from [0, 1]
def pageRank(M, d, thresh):

    # check validity of M
    for i in range(len(M[0])):
        if sum(M[:][i])!=0:
            print 'invalid M'
            return

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

M = np.asarray([[0, 0, 0, 0, 1], [ 0.5, 0, 0, 0, 0], [0.5, 0, 0, 0, 0], [ 0, 1, 0.5, 0, 0],[0, 0, 0.5, 1, 0]])
print pageRank(M, 0.8, 0.001)
