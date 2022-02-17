# given N items. w[i] is the weight, v[i] is the value
# given a knapsack with capacity of W max the total value. each item can be use 0 or 1 item
# NP-Complete

#search when n is small

weight = [3, 1, 2, 4]
values = [6, 10, 5, 10]

# dp[i][j]
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]] + w[i])
# dp[j] = max( dp[j], dp[j-c[i]] + w[i])
backpackWeight = 6

n = len(values)
table = [[0 for x in range(backpackWeight+1)] for x in range(n+1)]

for row in range(n+1):
    for col in range(backpackWeight+1):
        if row == 0 or col == 0:
            table[row][col] = 0                    
        elif weight[row-1] > col:
            table[row][col] = table[row-1][col]
        else:
            table[row][col] = max(
                table[row-1][col],
                table[row-1][col - weight[row-1]] + values[row-1]
            )

print(table[n][backpackWeight])

