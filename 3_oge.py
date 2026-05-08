# # Напишите наименьшее натуральное число x, для которого истинно высказывание:
# # (x > 11) И (x чётный) И ( x не делится на 3)
# for x in range(10000):
#     f = (x > 11) and (x % 2 ==0) and (x % 3 != 0)
#     if f == True:
#         print(x)
#
# Определите количество натуральных чисел x, для которых логическое выражение ложно:
# НЕ ((x < 8) И (x < 21)) ИЛИ (x нечётное)
#
#
# Определите количество целых двузначных чисел x  , для которых ЛОЖНО высказывание:
# (x четное) ИЛИ НЕ (x <  16)
# for x in range(1000):
#     f = not((x<8) and (x<21)) or (x % 2 !=0)
#     if f == False:
#         print(x)

# for x in range(1000):
#     f = (x % 2 ==0) or not(x < 16)
#     if f == False:
#         print(x)

# Напишите наименьшее натуральное число X, для которого ложно высказывание:
# ((x > 65) И (x < 80)) И (x чётный)

# for x in range (1000):
#     f = ((x > 65) and (x < 80)) and ( x % 2 ==0)
#     if f== False:
#         print(x)

# for x in range(1000):
#     f = not(x<4) and not(x>=9)
#     if f==True:
#         print(x)

# for x in range(1000):
#     f = (x  < 75 ) and not (x % 2 == 0)
#     if f== True:
#         print(x)
i = 0
for x in range(10,100):
    f = not (x % 2 ==0) and not (x > 39)
    if f == False:
        i+=1
print(i)
