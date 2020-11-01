n = int(input())
dp = [-1] * 100
dp[0] = 0
dp[1] = 1


def fibonacci(num):
    if dp[num] != -1:
        return dp[num]
    dp[num] = fibonacci(num - 1) + fibonacci(num - 2)
    return dp[num]


answer = fibonacci(n)
print(answer)
