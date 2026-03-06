# from math import *
# N = 510
# i = ceil(log(N,2))
# n = 862
# v = ceil(276) # kilo bait
# I = v / n
# L = I / i
# print(L)

# from math import *
# N = 963 + 52 + 10
# n = 2000
# v = 693 # kilo bait
# i = ceil(log(N, 2))
# I = floor(v * 1024 / n)
# L = floor(I * 8 / i)
# print(L)

from math import *
# N = 26+10 + 450
# n = 575
# v = 100 # kilo bait
# i = ceil(log(N, 2))
# I = floor(v * 1024 / n)
# L = ceil (I * 8 / i)
# print(L)

N = 7084 + 10
n = 22528
i = ceil (log2(N))
L = 5
I = ceil(L * i / 8)
V = n * I / 1024
print(V)
