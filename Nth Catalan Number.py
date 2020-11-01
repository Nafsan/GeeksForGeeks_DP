# Catalan numbers are a sequence of natural numbers that occurs in many interesting counting
# problems like following.
#
# 1. Count the number of expressions containing n pairs of parentheses which are correctly
# matched.
# For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
#
# 2) Count the number of possible Binary Search Trees with n keys (See this)
#
# 3) Count the number of full binary trees (A rooted binary tree is full if every vertex
# has either two children or no children) with n+1 leaves.
#
# 4) Given a number n, return the number of ways you can draw n chords in a circle with
# 2 x n points such that no 2 chords intersect. See this for more applications. The first few
# Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
n = int(input())


def nth_catalan_number(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j]
            dp[i] *= dp[i-j-1]
    return dp


answer = nth_catalan_number(n)
print(answer)