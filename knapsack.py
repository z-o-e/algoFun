class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class knapsack:
    def __init__(self, constraint, items):
        self.constraint  = constraint
        self.items = items
        self.dp = [[0 for i in range(len(self.items)+1)] for j in range(self.constraint+1)]

    def solve(self):
        for j in range(1,len(self.items)+1):
            for i in range(1, self.constraint+1):
                if i < self.items[j-1].weight:
                    self.dp[i][j] = self.dp[i-1][j]
                else:
                    print i,j,i-self.items[j-1].weight
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i-self.items[j-1].weight][j-1] + self.items[j-1].value)
        return self.dp[-1][-1]

    def backtrack(self):
        i,j = len(self.dp)-1, len(self.dp[0])-1
        select = []
        while j>=0 and self.dp[i][j]>0:
            if self.dp[i][j]!=self.dp[i][j-1]:
                select.append(self.items[j-1])
                i -= self.items[j-1].weight
            j -= 1
        return select

values = [3,2,4,4]
weights = [4,3,2,3]
items = []
for i in range(4):
    t = item(weights[i], values[i])
    items.append(t)
constraint = 6
test = knapsack(constraint, items)
test.solve()
test.backtrack()
                
