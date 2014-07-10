class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        levels = len(triangle)
        f = [ 0 for i in range(levels) ]
    
        for i in range(levels):
            # a new copy
            tmp = f[:]
            for idx in range(i+1):
                if idx==0:
                    f[idx] = tmp[idx] + triangle[i][idx]
                    print 'first', idx, f[idx],f
                elif idx == i:
                    f[idx] = tmp[idx-1]+triangle[i][idx]
                    print 'second', idx, f[idx],f
                else:
                    f[idx] = min(tmp[idx], tmp[idx-1])+triangle[i][idx]

        return min(f)
                