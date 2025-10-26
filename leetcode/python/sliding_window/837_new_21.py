class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
        if n >= k + maxPts - 1:
            return 1.0
        windowSum = 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1
        ans = 0.0
        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts
            if i < k:
                windowSum += dp[i]
            else:
                ans += dp[i]
            if i >= maxPts:
                windowSum -= dp[i - maxPts]
        return ans


s = Solution()
n = 6
k = 1
maxPts = 10
res = s.new21Game(n, k, maxPts)
print(res)
