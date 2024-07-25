def fib(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

#print(fib(10, [-1] * 100))


def fib2(n):
    dp = [0,1,1]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]


print(fib2(10))