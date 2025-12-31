# def fibonacci(n):
#     a, b = 0, 1
#     series = []
#     for _ in range(n):
#         series.append(a)
#         a,b = a+b ,a
#     return series
# print(fibonacci(10))

#####OUTPUT: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# def fib( n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(10))

#######OUTPUT: 55

# def fibonacci_series(n, a=0, b=1, series=None):
#     if series is None: 
#         series = []
#     if n == 0:
#         return series
#     series.append(a)  
#     return fibonacci_series(n-1, b, a+b, series) 
# print(fibonacci_series(10))

####OUTPUT: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# def fib(n ,memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fib(n-1 , memo) + fib(n-2 , memo)
#     return memo[n]

# print(fib(10))

# def fib(n):
#     if n <= 1:
#         return n
#     dp = [0,1]
#     for i in range(2 , n+1):
#         dp.append(dp[i-1] + dp[i-2])
#     return dp[n]

# n = 7 
# print(fib(n))