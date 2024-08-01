"""
Code for calculating fibonacci number for the given number using iterative method (normal method),
recursive method, and dynamic programming
"""
import time


def fib_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dp(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif not memo[n]:
        memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]


def fib_normal(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# execution time of normal fibonacci series
start_time = time.time()
fib_normal(3000)
print("\n---Execution time of normal fib = %s seconds ---\n" %
      (time.time() - start_time))

# execution time of recursive fibonacci series
start_time = time.time()
fib_rec(20)
print("\n---Execution time of recursive fib = %s seconds ---\n" %
      (time.time() - start_time))

# execution time of fibonacci series using dynamic programming
start_time = time.time()
n = 1000
memo = [None for i in range(n + 1)]
fib_dp(n, memo)
print("\n---Execution time of dynamic fib = %s seconds ---\n" %
      (time.time() - start_time))
