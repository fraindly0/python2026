# * модуль
# x = -42.42
# abs_x = abs(x)
# print(abs_x)

# * Импорт модулей
# print(math.pi)
# print(math.ceil(3.14))
# print(math.floor(3.14))

# ? from math import pi,ceil, floor
# print(pi)
# print(ceil(4.2))
# print(floor(4.9))

# ? from math import *
# print(pi)
# print(ceil(4.2))
# print(floor(4.9))

# import math as m
# print(m.pi)
# print(m.ceil(4.2))
# print(m.floor(4.9))

# from math import *
# print(ceil(4.2)) # окрругляет вверх
# print(floor(4.9)) # округляет вниз
# print(log2(32)) # логорифм с основанием 2
# print(log(32, 2)) # логорифмс уневерсальным основанием
#
# from random import *
# r = randint(0, 100)
# print(r)

# from math import *
# N = 239
# i = ceil (log2(N))
# print(i)
from math import *
# N=1030
# i = ceil(log2(N))
# print(i)

# N = 70
# L = 100
# from math import *
# i = ceil (log2(N))
# print (i)
# I = L * i / 8
# print (ceil(I))

# L = 317
# N = 4090+10
# n = 262144
# i = ceil (log2(N))
# I = ceil(L * i / 8)
# v = I * n / 1024 / 1024
# print(v)

# L = 5
# N = 7094
# n = 22528
# i = ceil(log2(N))
# I = ceil (L * i /8)
# v = I * n /1024
# print(v)

# n = int(input())
# total =  0
# for i in range(n):
#     num = int(input())
#     if num % 3 ==0:
#         total += num
# print(total)

# L = 15
# N = 8
# n = 20
# i = ceil(log(N,2))
# I = ceil ( L* i /8)
# v = I * n
# print(v)

# L = 101
# N = 4100
# n = 2048
# i = ceil(log(N,2))
# I = ceil ( L* i  / 8)
# v = I * n / 1024
# print(v)

# L = 252
# N = 1710
# n =  4096
# i = ceil(log(N,2))
# I = ceil(L * i / 8)
# v = I * n / 1024
# print(v)

L = 25
N = 26
n = 35
i = ceil(log(N,2))
I = ceil (L * i / 8)
v = I * n
print(v)