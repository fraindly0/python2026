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

# from math import *
# # N = 26+10 + 450
# # n = 575
# # v = 100 # kilo bait
# # i = ceil(log(N, 2))
# # I = floor(v * 1024 / n)
# # L = ceil (I * 8 / i)
# # print(L)
#
# N = 7084 + 10
# n = 22528
# i = ceil (log2(N))
# L = 5
# I = ceil(L * i / 8)
# V = n * I / 1024
# print(V)

# total = int(input())
# max = 0
# min = 300
# for i in range(total):
#     num = int(input())
#     if max < num:
#         max = num
#     if min > num:
#         nin = num
# print(max)
# if min > 30:
#     print("No")
# else:
#     print("Yes")

# total = int(input())
# sdalo = 0
# summa = 0
# for i in range(total):
#     zadachi = int(input())
#     if zadachi > 8:
#         sdalo += 1
#         summa += zadachi
# print(sdalo)
# print(summa / sdalo)

sum = 0
ccaunt=0
while True:
    total = int(input())
    if total == 0:
        break
    if total % 10 == 1:
        sum += total
        ccaunt += 1
if sum == 0:
    print("No")
else:
    print(sum/ccaunt)
