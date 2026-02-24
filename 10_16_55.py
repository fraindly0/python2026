# Напишите программу подсчёта суммы цифр в записи натурального числа.
# На вход программе подаётся натуральное число. Программа должна напечатать только одно число - сумму цифр

# n=int(input())
# s = 0
# while n > 0:
#     k = n % 10
#     s +=k
#     n = n // 10
# print(s)

#1
# n = int(input())
# w = 0
# while n > 0:
#     k = n % 10
#     if k % 3 == 0:
#         w += 1
#     n =  n // 10
# print(w)

#2
# n = int(input())
# w = 0
# while n > 0:
#     k = n % 10
#     if k % 4 == 0:
#         w += 1
#     n =  n // 10
# print(w)

#3
# n = int(input())
# w =0
# while n != 0:
#     n = int(input())
#     if n % 10 == 4 and n % 6 ==0:
#         w += n
# print(w)

#4
# w = 0
# n = int(input())
# while n != 0:
#     if n % 4 == 0 or n % 9 == 0:
#         w += n
#     n = int(input())
# print(w)

#5
# n = int(input())
# w=0
# while n != 0:
#     k = n % 10
#     if k % 4 != 0:
#         w += k
#     n = n // 10
# print(w)

#6
# n = int(input())
# w=0
# while n != 0:
#     k= n % 10
#     if k % 3 != 0:
#         w += k
#     n = n // 10
# print(w)

#7
# n = int(input())
# w = 0
# while n != 0:
#     k = n % 10
#     if k>7:
#         w +=k
#     n = n // 10
# print(w)

#8
# n = int(input())
# w = 0
# while n != 0:
#     if n % 4 == 0:
#         w +=n
#     n = int(input())
# print(w)

#9
# n = int(input())
# w = 0
# while n != 0 :
#     k = n % 10
#     if k<6 :
#         w += k
#     n = n //10
# print(w)

n = int(input())
total = 0
for i in range(n):
    a = int(input())
    if a // 4 % 4 == 3:
        total += a
print(total)
