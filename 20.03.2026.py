# ? Практика

'''
#На предприятии каждой изготовленной детали присваивают серийный номер, содержащий десятичные цифры и
символы из 17-символьного специального алфавита. В базе данных каждый серийный номер занимает одинаковое
и минимально возможное число байт. При этом используется посимвольное кодирование серийных номеров,
все символы кодируются одинаковым и минимально возможным числом бит. Известно, что для хранения
7 564 230 серийных номеров требуется более 31 Мбайт памяти.
Определите минимально возможную длину серийного номера
'''
from math import ceil, log2, floor

N = 17 + 10
i = ceil(log2(N))
n = 7564230
V = 31 * 2 ** 20
for L in range (1, 100) :
    I = ceil(L * i / 8 )
    if n * I > V :
        print(L)
        break

N = 25 + 487
i = ceil(log2(N))
n = 345
V = 70 * 1024
for L in range (1, 10000) :
    I = ceil(L * i / 8 )
    if n * I > V :
        print(L)
        break

L = 20
n = 600000
V = 11 *1024 * 1024
for i in range (1, 10000) :
    I = ceil(L * i / 8 )
    if n * I > V :
        print(i)
        break

L = 23
N = 62
i = ceil(log2(N))
V = 20
I = ceil(L * i / 8 ) + 10
for n in range (1, 100000) :
    if n * I / 1024 >= V :
        print(n)
        break

L = 250
N = 1660
i = ceil(log2(N))
I = ceil(L * i / 8 )
n = 65536
print( I, i )
for V in range (1, 1000000000000000000000000000) :
    if V * 1024 /n == I :
        print(V)
        break

V = 213 * 1024
N = 36 + 450 + 10
i = ceil(log2(N))
n = 708
for L in range (1, 100000) :
    I = ceil(L * i / 8 )
    if n * I > V :
        print(L)
        break

N = 52 + 963 + 10
V = 693 * 1024
n = 2000
i = ceil(log2(N))
for L in range (100000, 1,-1) :
    I = ceil(L * i / 8 )
    if n * I < V :
        print(L)
        break

L = 1231
V = 432 * 1024
n = 523872
for N in range (1, 10000) :
    i = ceil(log2(N))
    I = ceil(I * i / 8 )
    if n * I > V :
        print(N)
        break
