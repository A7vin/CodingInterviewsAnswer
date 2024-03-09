
# 有n级台阶，每次你可以跳1级或2级，问有多少种不同的方法可以跳到最顶端。
def climb_stairs_2(n):
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# 有n级台阶，每次你可以跳1级、2级或3级台阶时，问有多少种不同的方法可以跳到最顶端。
def climb_stairs_3(n):
    if n <= 2:
        return n
    if n == 3:
        return 4

    dp = [0] * (n+1)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]
