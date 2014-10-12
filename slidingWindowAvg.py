# a large stream of integers, wondow of size N
# standing query: what is the average of the integers in the window?
def slidingAvg(N,stream):
    window = []
    # for the first N inputs, sum and count to get the average
    for i in range(N):
        window.append(stream[i])
    avg = 1.*sum(window)/N
    
    #afterwards, when a new input arrives, change the average by adding (i-j)/N, where j is the oldest number in the window
    for i in range(N,len(stream)):
        print avg, window
        oldest = window[0]
        avg += (stream[i]-oldest)*1./N
        window = window[1:]
        window.append(stream[i])

test = slidingAvg(3, [1,2,3,4,5,6,7,8,9])
