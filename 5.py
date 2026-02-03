# ? составные вырожения / (and, or)


# * И (and)
age = 25
balance = 1000
if age >= 18 and balance > 500:
    print("покупка разрешена")
else:
    print("Нелостаточно средств или мал возраст")

# * ИЛИ (or)
day = "sunday"
if day == "sunday" or day == "saturday":
    print("Выходной")
else:
    print("сегодня выходной")

# * НЕ (not)
is_danned = False
if not is_danned:
    print("Доступ рзрешено")
else:
    print("Доступ разрешон")

# ! порядок выполнения действий
# * ()
# * not
# * and
# * or

# ? вложенные конструкции
username = "fraindly10"
password = "1234567890"
if username == "fraindly10":
    print("логин пороль")
    if password == "1234567890":
        print("всё верно")
    else:
        print("Пороль не верный")
else:
    print("Логин не верный")

#1
# time=int(input("видите время"))
# if time>9 and time<21:
#     print("магазин открыт")
# else:
#     print("магазин закрыт")

#2
# diskontnaikarta=input("есть ли карта постоянного посетителя ")
# caunt=int(input("ведите на  сколько денег вы потратили"))
# if diskontnaikarta == "yes" and caunt>5000:
#     print("вы получаете скидку")
# else:
#     print("нет не дам скидку")



#4
x=int(input())
y=int(input())
if x>0 and y>0:
    print('1 chetvert')
elif x<0 and y<0:
    print('3 chetvert')
elif x>0 and y<0:
    print('4 chetvert')
else:
    print('2 chetvert')
    




