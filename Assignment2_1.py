# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:03:56 2024

@author: yentz
"""

import time
import matplotlib.pyplot as plt

# Top-down (recursive) approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
# Bottom-up (dynamic programming) approach
def fibonacci_dynamic(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


n_values = list(range(1, 100))
times_recursive = []
times_dynamic = []

# Measure execution time for F(1) to F(5)
for n in n_values:
    start_time = time.time()
    result = fibonacci_dynamic(n)
    end_time = time.time()
    times_dynamic.append(end_time - start_time)
    print(f"dy_F({n}) = {result}, Time: {end_time - start_time:.6f} seconds")
    
for n in n_values:
    start_time = time.time()
    result = fibonacci_recursive(n)
    end_time = time.time()
    times_recursive.append(end_time - start_time)
    print(f"re_F({n}) = {result}, Time: {end_time - start_time:.6f} seconds")