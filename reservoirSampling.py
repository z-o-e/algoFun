# reservoir sampling is randomized algorithm---when a stream exceeds the size, a subsample of k items are chosen, each with equal probability

import random

# @param stream: a list of elements
# @param n: an int of stream size
# @param k: an int of sampling size
def reservoirSampling(stream, n, k):
    reservoir = []
    for i in range(k):
        reservoir.append(stream[i])

    for i in range(k,n):
        # the j-th element is chosen to be replaced with pribability (1/k)*(k/i)=1/i, when finishing iterating the stream, each element would have k/n probability of being selected 
        # proof by induction, (k/(k+1))*((k+1)/(k+2))*...*(n-1)/n = k/n)
        j = random.randint(0,i)
        if j<k:
            reservoir[j] = stream[i]

    return reservoir

stream = range(12)
k = 5
reservoirSampling(stream, 12, k)
