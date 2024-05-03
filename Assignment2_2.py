# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:44:23 2024

@author: yentz
"""
import matplotlib.pyplot as plt

total_times_rec=0
total_times_dyn=0


# Bottom-up (dynamic programming) approach
def fibonacci_dynamic(n):
    global total_times_dyn
    fib = [0] * (n+1)
    fib[1] = 1
    
    for i in range(2, n+1):
        if(i==4):
            total_times_dyn +=1
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Top-down (recursive) approach
def fibonacci_recursive(n):
    global total_times_rec
    if n <= 1:
        return n
    else:
        if n-1 == 4:
            total_times_rec+=1
        if n-2 == 4:
            total_times_rec+=1
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

rec_times = []
dyn_times = []

for n in range(1,48): 
    dyn_result = fibonacci_dynamic(n)
    print(f"dynamic F({n})={dyn_result} 使用F(4){total_times_dyn}次")
    dyn_times.append(total_times_dyn)
    total_times_dyn=0
    
for n in range(1,48):
    rec_result = fibonacci_recursive(n)
    print(f"recursive F({n})={rec_result} 使用F(4){total_times_rec}次")
    rec_times.append(total_times_rec)
    total_times_rec=0
    

# 繪製折線圖
plt.plot(range(1, len(rec_times) + 1), rec_times,label='Recursive')
plt.plot(range(1, len(dyn_times) + 1), dyn_times,label='Dynamic')
plt.xlabel('n')
plt.ylabel('Times ')
plt.title('Times that F(4) used(n=100)')
plt.legend()
plt.show()
