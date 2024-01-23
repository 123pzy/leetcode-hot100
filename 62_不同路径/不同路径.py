# 突然想到解这个题的新思路，不用单独处理第一行和第一列
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n+=1
        m+=1
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        dp[1][0] = 1
        dp[0][1] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return int(dp[m-1][n-1]/2)

# 常规解法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]