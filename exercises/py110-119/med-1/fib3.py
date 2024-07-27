"""
Our recursive fibonacci function from the previous exercise isn't very efficient.
It starts slowing down with an nth argument value somewhere around 35-60, depending
on your system. One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

Memoization is an approach that involves saving a computed answer for future reuse,
instead of computing it from scratch every time it is needed. In the case of our
recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2)
because the necessary values have already been computed by the recursive calls to
fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci function
to use memoization.

An image representing the computation of the 7th Fibonacci number is shown below.
It is the same image that was shown in the previous exercise, except this one highlights
the values that have previously been computed.
"""

# ! REVISE memoization, this is the LS solution
memo = {}
def fibonacci(nth):
    if nth <= 2:
        return 1
    elif nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return memo[nth]