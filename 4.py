# ? boolean / bool / логический тип данных
my_bool_1 = True
my_bool_2 = False
print(my_bool_1 or my_bool_2)

# ? логический оператор
print(5>3)
print(5>=3)
print(5<3)
print(5<=3)
print(5==3)
print(5!=3)

# ? условные операторы / if-elif-else
# * 1. if (если)
num = 10
if num > 0:
    print("число положительное")

# * 2. if-else (если-иначе)
age = 12
if age >= 12:
    print("доступ разрешон")
else:
    print("доступ запрешён")

# * 2. if-else-else (если-иначе ессли - иначи)
color = "yellow"
if color == "green":
    print("едем")
elif color == 'yellow':
    print("ждём")
else:
    print ('Стоим')

#1
# num1 = int(input())
# if num1 > 0:
#     print("плюс")
# else:
#     print("minus")

#2
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print(num1,num2)

#3
num1 = int(input())
if num1 % 2 == 0:
    print("чётное")
else:
    print("нечётное")

#4
num1 = int(input())
if num1 % 10 == 0:
    print("оканчивается на 0")
else:
    print('не оканчивается на 0')

#5
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1+num2 > num3 and num1+num3 > num2 and num3+num2 > num1:
    print('можно построить')
else:
    print('нельзя построить')

#6
num1 = int(input())
if num1 > 90:
    print('отлично')
elif num1 > 70 and num1 < 89:
    print("хорошо")
elif num1 > 50 and num1 < 69:
    print('удавлетворительно')
else:
    print('не сдал')
#7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = int(input())
if a<=n<=a+b and b<=n<=b+c and c<=n<=c+d:
    print()

